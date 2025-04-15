import socket
import time

from ping3 import ping

import psutil
from ping3.errors import PingError


class Network:
    def __init__(self):
        pass

    @staticmethod
    def get_network_names():
        """"
        Get the names of all network interfaces on the system
        
        :return: A list of network interface names
        """
        return psutil.net_if_addrs().keys()

    @staticmethod
    def get_network_interfaces(name: str = None) -> list[dict]:
        """
        Get a list of network interfaces
        
        :param name: The network interface name
        :return: List of network interfaces represented as dicts
        """
        network_interfaces = []

        for interface, snicaddrs in psutil.net_if_addrs().items():

            if name is not None and name != interface:
                continue

            network_info = {
                'name': interface,
                'ipv4': None,
                'ipv6': None,
                'mac': None,
            }
            for snicaddr in snicaddrs:
                if snicaddr.family == socket.AF_INET:
                    network_info['ipv4'] = snicaddr.address
                elif snicaddr.family == socket.AF_INET6:
                    network_info['ipv6'] = snicaddr.address
                elif snicaddr.family == psutil.AF_LINK:
                    network_info['mac'] = snicaddr.address

            network_interfaces.append(network_info)

        return network_interfaces

    @staticmethod
    def get_network_statuses(name: str = None) -> list[dict]:

        """
        Get a list of network interface statuses
        
        :param name: The network interface name to get
        :return: A list of network interface statuses represented as dicts
        """

        network_statuses = []

        for interface, snicstats in psutil.net_if_stats().items():

            if name is not None and name != interface:
                continue

            duplex_map = {
                psutil.NIC_DUPLEX_FULL: "full",
                psutil.NIC_DUPLEX_HALF: "half",
                psutil.NIC_DUPLEX_UNKNOWN: "unknown"
            }
            duplex_str = duplex_map.get(snicstats.duplex)

            network_status = \
                {
                    'name': interface,
                    'is_up': snicstats.isup,
                    'duplex': duplex_str,
                    'speed': snicstats.speed,
                    'mtu': snicstats.mtu
                }

            network_statuses.append(network_status)

        return network_statuses

    @staticmethod
    def get_network_packet_send() -> int:
        """
        Get number of send packets
        
        :return: A number of send packets
        """
        return psutil.net_io_counters().packets_sent

    @staticmethod
    def get_network_packet_received() -> int:
        """
        Get number of received packets
        :return: A number of received packets
        """
        return psutil.net_io_counters().packets_recv

    @staticmethod
    def get_network_packet_dropped() -> dict:
        """
        Get the number of dropped packets for sent and received data
        
        :return: A dictionary with dropped packets for sent and received data
        """
        io_counters = psutil.net_io_counters()
        return {
            'dropped_sent': io_counters.dropout,
            'dropped_received': io_counters.dropin
        }

    @staticmethod
    def get_network_bandwidth_upload(interval: int = 1) -> float:
        """
        Calculate the upload bandwidth in bytes per second

        :param interval: Time interval in seconds to measure bandwidth defaults to 1 second
        :return: Upload bandwidth in bytes per second
        """

        initial_byte_send = psutil.net_io_counters().bytes_sent
        time.sleep(interval)
        timeout_byte_send = psutil.net_io_counters().bytes_sent

        return (timeout_byte_send - initial_byte_send) / interval

    @staticmethod
    def get_network_bandwidth_download(interval: int = 1) -> float:
        """
        Calculate the download bandwidth in bytes per second

        :param interval: Optional; Time interval in seconds to measure bandwidth defaults to 1 second
        :return: Download bandwidth in bytes per second
        """

        initial_byte_recv = psutil.net_io_counters().bytes_recv
        time.sleep(interval)
        timeout_byte_recv = psutil.net_io_counters().bytes_recv

        return (timeout_byte_recv - initial_byte_recv) / interval

    @staticmethod
    def get_network_latency(destination_host: str = 'google.com', n: int = 3, timeout: int = 3,
                            unit: str = 'ms') -> float:
        """
        Measure the average network latency to a specified destination host

        Args:
            destination_host: The host to ping default('google.com')
            n: The number of ping attempts default(3)
            timeout: The timeout for each ping in seconds default(3)
            unit: The unit of latency measurement ('ms' for milliseconds, 's' for seconds) default('ms')

        Returns:
            float: The average latency in the specified unit, rounded to 2 decimal places
                   Returns -1.0 if all ping attempts fail.

        Raises:
            PingError: If a ping attempt fails
        """
        latency = []

        for i in range(n):
            try:
                result = ping(destination_host, timeout=timeout, unit=unit)
                if result is not None:
                    latency.append(result)
            except PingError as e:
                print(f"Ping attempt {i + 1} failed: {e}")

        if sum(latency) == 0:
            print(f"All ping attempts to {destination_host} failed")
            return float(0)

        average_latency = sum(latency) / len(latency)
        return round(average_latency, 2)