# Zabbix Clone Project - Client

## Overview

Zabbix is a monitoring solution for networks and applications. This project is a clone of Zabbix, which is a popular open-source monitoring solution. The goal of this project is to provide similar functionality to Zabbix but with a custom implementation.

## Features

### 1. System Metrics
- **CPU**:
  - Total CPU usage percentage.
  - Per-core CPU utilization.
  - Load average (1, 5, 15 minutes).

### 2. Error Handling
- Handles unsupported platform errors for load averages.
- Catches unexpected exceptions and provides meaningful error messages.

## Current Implementation

### Modules
- **CPU Monitoring**:
  - `CPU.get_cpu_usage(interval: int)`: Returns total CPU usage percentage over a specified interval.
  - `CPU.get_per_core_usage(interval: int)`: Returns per-core CPU usage percentages over a specified interval.
  - `CPU.get_load_average()`: Returns system load averages for the last 1, 5, and 15 minutes. Handles unsupported platforms gracefully.

### CLI Application
- A simple command-line interface (`client/src/main.py`) to display CPU metrics in real-time, including:
  - Total CPU usage.
  - Per-core utilization.
  - Load averages.

## Requirements

- **Python**: 3.13 or higher
- **Dependencies**:
  - `psutil`: For retrieving system metrics.

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd zabbix_client
   
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python client/src/main.py
    ```