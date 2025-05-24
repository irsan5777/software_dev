import random
import time
import json
from datetime import datetime, timedelta
from collections import defaultdict, deque
import threading
import ipaddress

class NetworkPacket:
    """Represents a network packet with relevant attributes"""
    def __init__(self, src_ip, dst_ip, src_port, dst_port, protocol, packet_size, timestamp=None):
        self.src_ip = src_ip
        self.dst_ip = dst_ip
        self.src_port = src_port
        self.dst_port = dst_port
        self.protocol = protocol
        self.packet_size = packet_size
        self.timestamp = timestamp or datetime.now()
    
    def to_dict(self):
        return {
            'src_ip': self.src_ip,
            'dst_ip': self.dst_ip,
            'src_port': self.src_port,
            'dst_port': self.dst_port,
            'protocol': self.protocol,
            'packet_size': self.packet_size,
            'timestamp': self.timestamp.isoformat()
        }

class DummyDataGenerator:
    """Generates realistic dummy network traffic data"""
    
    def __init__(self):
        self.internal_ips = [
            '192.168.1.{}'.format(i) for i in range(1, 51)
        ]
        self.external_ips = [
            '203.0.113.{}'.format(i) for i in range(1, 100)
        ]
        self.common_ports = [80, 443, 22, 21, 23, 53, 25, 110, 143, 993, 995]
        self.protocols = ['TCP', 'UDP', 'ICMP']
        
        # Malicious patterns
        self.malicious_ips = ['203.0.113.66', '203.0.113.77', '203.0.113.88']
        self.attack_ports = [1433, 3389, 445, 139, 135]
    
    def generate_normal_packet(self):
        """Generate a normal network packet"""
        src_ip = random.choice(self.internal_ips + self.external_ips)
        dst_ip = random.choice(self.internal_ips)
        src_port = random.randint(1024, 65535)
        dst_port = random.choice(self.common_ports)
        protocol = random.choice(self.protocols)
        packet_size = random.randint(64, 1500)
        
        return NetworkPacket(src_ip, dst_ip, src_port, dst_port, protocol, packet_size)
    
    def generate_port_scan_attack(self):
        """Generate port scanning attack packets"""
        attacker_ip = random.choice(self.malicious_ips)
        target_ip = random.choice(self.internal_ips)
        src_port = random.randint(1024, 65535)
        dst_port = random.randint(1, 1024)  # Scanning low ports
        protocol = 'TCP'
        packet_size = random.randint(40, 80)  # Small packets for scanning
        
        return NetworkPacket(attacker_ip, target_ip, src_port, dst_port, protocol, packet_size)
    
    def generate_ddos_attack(self):
        """Generate DDoS attack packets"""
        attacker_ip = random.choice(self.malicious_ips)
        target_ip = random.choice(self.internal_ips)
        src_port = random.randint(1024, 65535)
        dst_port = random.choice([80, 443])  # Target web services
        protocol = random.choice(['TCP', 'UDP'])
        packet_size = random.randint(1000, 1500)  # Large packets
        
        return NetworkPacket(attacker_ip, target_ip, src_port, dst_port, protocol, packet_size)
    
    def generate_brute_force_attack(self):
        """Generate brute force attack packets"""
        attacker_ip = random.choice(self.malicious_ips)
        target_ip = random.choice(self.internal_ips)
        src_port = random.randint(1024, 65535)
        dst_port = random.choice([22, 23, 21, 3389])  # Common login services
        protocol = 'TCP'
        packet_size = random.randint(100, 300)
        
        return NetworkPacket(attacker_ip, target_ip, src_port, dst_port, protocol, packet_size)
    
    def generate_packet(self):
        """Generate a random packet (normal or malicious)"""
        packet_type = random.choices(
            ['normal', 'port_scan', 'ddos', 'brute_force'],
            weights=[85, 5, 5, 5]  # 85% normal, 15% attacks
        )[0]
        
        if packet_type == 'normal':
            return self.generate_normal_packet(), 'normal'
        elif packet_type == 'port_scan':
            return self.generate_port_scan_attack(), 'port_scan'
        elif packet_type == 'ddos':
            return self.generate_ddos_attack(), 'ddos'
        else:
            return self.generate_brute_force_attack(), 'brute_force'

class IntrusionDetectionSystem:
    """Main IDS class that analyzes network traffic"""
    
    def __init__(self):
        self.packet_buffer = deque(maxlen=1000)  # Store last 1000 packets
        self.connection_tracker = defaultdict(int)  # Track connections per IP
        self.port_scan_tracker = defaultdict(set)  # Track unique ports per IP
        self.traffic_volume = defaultdict(int)  # Track traffic volume per IP
        self.alerts = []
        self.running = False
        
        # Detection thresholds
        self.PORT_SCAN_THRESHOLD = 10  # Unique ports accessed
        self.CONNECTION_THRESHOLD = 50  # Connections per minute
        self.TRAFFIC_THRESHOLD = 100000  # Bytes per minute
        self.TIME_WINDOW = 60  # seconds
        
    def add_packet(self, packet):
        """Add a packet to the analysis buffer"""
        self.packet_buffer.append(packet)
        self.update_trackers(packet)
    
    def update_trackers(self, packet):
        """Update various tracking metrics"""
        current_time = packet.timestamp
        src_ip = packet.src_ip
        
        # Update connection tracker
        self.connection_tracker[src_ip] += 1
        
        # Update port scan tracker
        self.port_scan_tracker[src_ip].add(packet.dst_port)
        
        # Update traffic volume
        self.traffic_volume[src_ip] += packet.packet_size
        
        # Clean old entries (older than time window)
        self.cleanup_old_entries(current_time)
    
    def cleanup_old_entries(self, current_time):
        """Remove entries older than the time window"""
        cutoff_time = current_time - timedelta(seconds=self.TIME_WINDOW)
        
        # Remove old packets
        while self.packet_buffer and self.packet_buffer[0].timestamp < cutoff_time:
            self.packet_buffer.popleft()
    
    def detect_port_scan(self, src_ip):
        """Detect port scanning attacks"""
        unique_ports = len(self.port_scan_tracker[src_ip])
        if unique_ports >= self.PORT_SCAN_THRESHOLD:
            return {
                'type': 'Port Scan',
                'severity': 'HIGH',
                'src_ip': src_ip,
                'unique_ports': unique_ports,
                'description': f'IP {src_ip} accessed {unique_ports} unique ports'
            }
        return None
    
    def detect_ddos(self, src_ip):
        """Detect DDoS attacks based on connection volume"""
        connections = self.connection_tracker[src_ip]
        if connections >= self.CONNECTION_THRESHOLD:
            return {
                'type': 'DDoS',
                'severity': 'CRITICAL',
                'src_ip': src_ip,
                'connections': connections,
                'description': f'IP {src_ip} made {connections} connections in {self.TIME_WINDOW}s'
            }
        return None
    
    def detect_traffic_anomaly(self, src_ip):
        """Detect unusual traffic volume"""
        volume = self.traffic_volume[src_ip]
        if volume >= self.TRAFFIC_THRESHOLD:
            return {
                'type': 'Traffic Anomaly',
                'severity': 'MEDIUM',
                'src_ip': src_ip,
                'volume': volume,
                'description': f'IP {src_ip} generated {volume} bytes in {self.TIME_WINDOW}s'
            }
        return None
    
    def detect_brute_force(self, src_ip):
        """Detect brute force attacks on authentication services"""
        auth_ports = {22, 23, 21, 3389, 1433}
        connections_to_auth = 0
        
        for packet in self.packet_buffer:
            if packet.src_ip == src_ip and packet.dst_port in auth_ports:
                connections_to_auth += 1
        
        if connections_to_auth >= 20:  # 20+ auth attempts
            return {
                'type': 'Brute Force',
                'severity': 'HIGH',
                'src_ip': src_ip,
                'auth_attempts': connections_to_auth,
                'description': f'IP {src_ip} made {connections_to_auth} authentication attempts'
            }
        return None
    
    def analyze_traffic(self):
        """Perform comprehensive traffic analysis"""
        alerts = []
        
        # Get unique source IPs from recent traffic
        recent_ips = set()
        for packet in self.packet_buffer:
            recent_ips.add(packet.src_ip)
        
        # Run detection algorithms for each IP
        for src_ip in recent_ips:
            # Port scan detection
            alert = self.detect_port_scan(src_ip)
            if alert:
                alerts.append(alert)
            
            # DDoS detection
            alert = self.detect_ddos(src_ip)
            if alert:
                alerts.append(alert)
            
            # Traffic anomaly detection
            alert = self.detect_traffic_anomaly(src_ip)
            if alert:
                alerts.append(alert)
            
            # Brute force detection
            alert = self.detect_brute_force(src_ip)
            if alert:
                alerts.append(alert)
        
        return alerts
    
    def generate_alert(self, alert):
        """Generate and store security alert"""
        alert['timestamp'] = datetime.now().isoformat()
        alert['id'] = len(self.alerts) + 1
        self.alerts.append(alert)
        
        # Print alert to console
        print(f"\n🚨 SECURITY ALERT #{alert['id']} 🚨")
        print(f"Type: {alert['type']}")
        print(f"Severity: {alert['severity']}")
        print(f"Source IP: {alert['src_ip']}")
        print(f"Description: {alert['description']}")
        print(f"Timestamp: {alert['timestamp']}")
        print("-" * 50)
    
    def get_statistics(self):
        """Get current IDS statistics"""
        total_packets = len(self.packet_buffer)
        unique_ips = len(set(packet.src_ip for packet in self.packet_buffer))
        total_alerts = len(self.alerts)
        
        severity_counts = defaultdict(int)
        for alert in self.alerts:
            severity_counts[alert['severity']] += 1
        
        return {
            'total_packets_analyzed': total_packets,
            'unique_source_ips': unique_ips,
            'total_alerts': total_alerts,
            'alerts_by_severity': dict(severity_counts),
            'active_connections': len(self.connection_tracker),
            'monitoring_window': f"{self.TIME_WINDOW} seconds"
        }

class IDSMonitor:
    """Main IDS monitoring system"""
    
    def __init__(self):
        self.ids = IntrusionDetectionSystem()
        self.data_generator = DummyDataGenerator()
        self.running = False
    
    def start_monitoring(self, duration=60):
        """Start the IDS monitoring system"""
        print("🛡️  Network Intrusion Detection System Started 🛡️")
        print("=" * 60)
        print(f"Monitoring network traffic for {duration} seconds...")
        print("Press Ctrl+C to stop monitoring\n")
        
        self.running = True
        start_time = time.time()
        packet_count = 0
        
        try:
            while self.running and (time.time() - start_time) < duration:
                # Generate dummy network packet
                packet, actual_type = self.data_generator.generate_packet()
                packet_count += 1
                
                # Add packet to IDS
                self.ids.add_packet(packet)
                
                # Analyze traffic every 10 packets
                if packet_count % 10 == 0:
                    alerts = self.ids.analyze_traffic()
                    for alert in alerts:
                        self.ids.generate_alert(alert)
                
                # Display progress every 50 packets
                if packet_count % 50 == 0:
                    print(f"📊 Processed {packet_count} packets...")
                
                # Simulate real-time traffic (small delay)
                time.sleep(0.1)
                
        except KeyboardInterrupt:
            print("\n⏹️  Monitoring stopped by user")
        
        self.running = False
        self.display_final_report()
    
    def display_final_report(self):
        """Display final monitoring report"""
        print("\n" + "=" * 60)
        print("📋 FINAL IDS REPORT")
        print("=" * 60)
        
        stats = self.ids.get_statistics()
        
        print(f"Total Packets Analyzed: {stats['total_packets_analyzed']}")
        print(f"Unique Source IPs: {stats['unique_source_ips']}")
        print(f"Total Security Alerts: {stats['total_alerts']}")
        print(f"Active Connections Tracked: {stats['active_connections']}")
        print(f"Monitoring Window: {stats['monitoring_window']}")
        
        if stats['alerts_by_severity']:
            print("\nAlerts by Severity:")
            for severity, count in stats['alerts_by_severity'].items():
                print(f"  {severity}: {count}")
        
        if self.ids.alerts:
            print(f"\n🔍 Recent Alerts (Last 5):")
            for alert in self.ids.alerts[-5:]:
                print(f"  [{alert['severity']}] {alert['type']}: {alert['description']}")
        
        print("\n✅ IDS monitoring completed successfully!")

def main():
    """Main function to run the IDS"""
    print("🛡️  Network Intrusion Detection System (IDS)")
    print("=" * 50)
    print("This IDS monitors network traffic and detects:")
    print("• Port Scanning Attacks")
    print("• DDoS Attacks") 
    print("• Traffic Anomalies")
    print("• Brute Force Attacks")
    print("\n" + "=" * 50)
    
    try:
        duration = int(input("Enter monitoring duration in seconds (default 60): ") or "60")
    except ValueError:
        duration = 60
    
    monitor = IDSMonitor()
    monitor.start_monitoring(duration)

if __name__ == "__main__":
    main()
    