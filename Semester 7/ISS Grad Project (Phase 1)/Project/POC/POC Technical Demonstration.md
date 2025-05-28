---
title: POC Technical Demonstration
author:
  - Jon Marien
created: 2025-03-25
published: 2025-03-25
tags:
  - capstone
---

| Title                       | Author                       | Created        | Published      | Tags                     |
| --------------------------- | ---------------------------- | -------------- | -------------- | ------------------------ |
| POC Technical Demonstration | <ul><li>Jon Marien</li></ul> | March 25, 2025 | March 25, 2025 | [[#capstone\|#capstone]] |

1. **Core Technology Stack**:
    - **Hardware**:
        - HackRF One: Software-defined radio for RF signal monitoring
        - OpenXC Vehicle Interface: For vehicle data collection
    - **Software**:
        - Python-based with key libraries:
            - pyrtlsdr: For RTL-SDR support
            - numpy/scipy: For signal processing
            - matplotlib/plotly/dash: For visualization
            - pandas: For data handling
              
2. **System Architecture**:
    - **RF Signal Detection Module**: Monitors automotive frequency ranges (315MHz and 433MHz)
    - **Vehicle Integration Module**: Uses OpenXC to collect real-time vehicle data
    - **Monitoring & Alerting System**: Provides dashboard visualization and alert generation
      
3. **Key Features**:
    - Real-time RF signal monitoring
    - Detection of suspicious activities (key fob relay attacks, cloning attempts)
    - Historical logging and analysis
    - Mobile companion app support
    - Comprehensive visualization dashboard
      
4. **Logging System**:
    - Maintains logs in `src/logs/dashboard` and `src/logs/integrated`
    - Tracks RF signal data and vehicle information
    - Stores detection history and alerts
      
5. **Simulation Environment**:
    - Supports both physical hardware and simulation modes
    - Can use OpenXC Vehicle Interface simulator
    - Allows testing without physical vehicle connection1. **Core Technology Stack**:
    - **Hardware**:
        - HackRF One: Software-defined radio for RF signal monitoring
        - OpenXC Vehicle Interface: For vehicle data collection
    - **Software**:
        - Python-based with key libraries:
            - pyrtlsdr: For RTL-SDR support
            - numpy/scipy: For signal processing
            - matplotlib/plotly/dash: For visualization
            - pandas: For data handling
              
6. **System Architecture**:
    - **RF Signal Detection Module**: Monitors automotive frequency ranges (315MHz and 433MHz)
    - **Vehicle Integration Module**: Uses OpenXC to collect real-time vehicle data
    - **Monitoring & Alerting System**: Provides dashboard visualization and alert generation
      
7. **Key Features**:
    - Real-time RF signal monitoring
    - Detection of suspicious activities (key fob relay attacks, cloning attempts)
    - Historical logging and analysis
    - Mobile companion app support
    - Comprehensive visualization dashboard
      
8. **Logging System**:
    - Maintains logs in `src/logs/dashboard` and `src/logs/integrated`
    - Tracks RF signal data and vehicle information
    - Stores detection history and alerts
      
9. **Simulation Environment**:
    - Supports both physical hardware and simulation modes
    - Can use OpenXC Vehicle Interface simulator
    - Allows testing without physical vehicle connection

10. `main_application.py`:

- **Purpose**: Main entry point and application controller
- **Key Components**:
    - `AutoSecurityPOC` class:
        - Manages the application's main interface
        - Handles user input through a command-line menu
        - Integrates with the RF detector and dashboard
    - Main menu options:
        1. Run Integrated RF Detector
        2. Show Dashboard (Simulation)
        3. View Documentation
        4. Exit
    - Uses rich library for styled console output
    - Implements a simple CLI interface with user prompts

2. `dashboard.py`:

- **Purpose**: Implements the visualization dashboard for RF signal monitoring
- **Key Components**:
    - `RFDashboard` class:
        - Manages real-time visualization of RF signals
        - Tracks vehicle data and alerts
        - Implements logging functionality
        - Features:
            - Signal strength monitoring
            - Vehicle status tracking
            - Alert generation
            - System status monitoring
    - Simulation features:
        - Generates simulated RF signals
        - Creates realistic vehicle data
        - Maintains alert history
        - Logs all activities
    - Uses rich library for advanced console visualization
        - Tables for data display
        - Panels for organized information
        - Live updates for real-time monitoring

3. `**init**.py`:

- **Purpose**: Package initialization file
- **Functionality**:
    - Makes the src directory a Python package
    - Allows importing modules from other locations
    - Typically empty or contains package-level imports

**Technical Integration**:

- The files work together in a layered architecture:
    1. `main_application.py` serves as the application's controller
    2. `dashboard.py` provides visualization and data processing
    3. The package structure allows for modular development and easy extension

**Key Technical Features**:

- Real-time data processing and visualization
- Logging system with timestamped entries
- Configurable parameters (duration, attack probability, thresholds)
- Integration with external systems (HackRF, OpenXC)
- Simulation capabilities for testing and demonstration

1. **Integration Directory**:

- `integrated_detector.py`:
    - **Purpose**: Core integration layer that combines HackRF and OpenXC functionality
    - **Key Features**:
        - Implements `IntegratedRFDetector` class
        - Manages both hardware (HackRF) and simulation (OpenXC) components
        - Provides real-time visualization of both systems
        - Implements logging with timestamps
        - Configurable parameters:
            - Duration
            - Signal strength threshold
            - Attack probability
    - **Architecture**:
        - Uses threading for concurrent operations
        - Implements rich console interface with layouts and panels
        - Maintains separate tables for simulator and detector data
        - Provides synchronized updates through table locks

2. **HackRF Directory**:

- `rf_detector.py`:
    - **Purpose**: Implements the HackRF One hardware interface
    - **Key Features**:
        - Implements `RFDetector` class
        - Monitors specific frequency ranges (315-433 MHz)
        - Detects and analyzes RF signals
        - Implements threshold-based alerting
    - **Technical Details**:
        - Uses numpy for signal processing
        - Implements real-time signal detection
        - Provides configurable parameters:
            - Frequency range
            - Signal strength threshold
            - Detection duration
        - Includes logging functionality
- `keyfob_detector.grc`:
    - **Purpose**: GNU Radio Companion configuration file
    - **Functionality**:
        - Defines the signal processing flow for key fob detection
        - Configures HackRF One parameters
        - Implements signal processing blocks

3. **OpenXC Directory**:

- `rf_simulator.py`:
    - **Purpose**: Implements the OpenXC simulation environment
    - **Key Features**:
        - Implements `RFDetector` class
        - Provides simulation of RF signals
        - Generates realistic vehicle data
        - Implements signal strength variations
    - **Technical Details**:
        - Simulates both normal and suspicious signals
        - Maintains configurable parameters:
            - Frequency range
            - Signal strength thresholds
            - Detection duration
        - Implements logging for simulation data
        - Uses numpy for signal generation

# Summary

1. **main_application.py**: This file serves as the application's entry point and controller. It features the `AutoSecurityPOC` class, which manages the command-line interface and user interactions. The main menu offers four key options:
	- Run Integrated RF Detector
	- Show Dashboard (Simulation)
	- View Documentation
	- Exit
	The application uses rich library for styled console output, providing a professional interface with prompts and choices.
2. **dashboard.py**: This file implements the visualization dashboard through the `RFDashboard` class. It offers comprehensive monitoring features:
	- Real-time RF signal visualization
	- Vehicle status tracking2
	- 
	- Alert generation and logging
	- System status monitoring
3. **Hardware Interface (HackRF)**: The system uses HackRF One for real-time RF signal detection, focusing on automotive frequencies (315-433 MHz). The `rf_detector.py` manages hardware communication and signal processing, while `keyfob_detector.grc` configures GNU Radio for key fob detection.
4. **Simulation Environment (OpenXC)**: The `rf_simulator.py` provides a realistic simulation environment for testing and development. It generates both normal and suspicious signals, allowing developers to test the system without physical hardware.
5. **Integration Layer**: The `integrated_detector.py` combines both hardware and simulation components. It manages real-time visualization, logging, and alert generation. The system uses rich console interfaces for professional-looking output and implements configurable parameters for threshold-based alerting.