## **NXP Semiconductors** 

Data Sheet: Technical Data 

## **i.MX RT1060 Crossover Processors for Consumer Products** 

## **1 i.MX RT1060 Introduction** 

The i.MX RT1060 is a new processor family featuring NXP’s advanced implementation of the Arm Cortex®-M7 core, which operates at speeds up to 600 MHz to provide high CPU performance and best real-time response. 

The i.MX RT1060 processor has 1 MB on-chip RAM. 512 KB can be flexibly configured as TCM or general purpose on-chip RAM, while the other 512 KB is general-purpose on-chip RAM. The i.MX RT1060 integrates advanced power management module with DCDC and LDO that reduces complexity of external power supply and simplifies power sequencing. The i.MX RT1060 also provides various memory interfaces, including SDRAM, RAW NAND FLASH, NOR FLASH, SD/eMMC, Quad SPI, and a wide range of other interfaces for connecting peripherals, such as WLAN, Bluetooth™, GPS, displays, and camera sensors. The i.MX RT1060 has rich audio and video features, including LCD display, basic 2D graphics, camera interface, SPDIF, and I2S audio interface. The i.MX RT1060 has analog interfaces, such as ADC, ACMP, and TSC. 

Document Number: IMXRT1060CEC 

## Rev. 4, 04/2024 

**==> picture [52 x 21] intentionally omitted <==**

**==> picture [51 x 28] intentionally omitted <==**

**MIMXRT1061DVL6A MIMXRT1061DVL6B MIMXRT1061DVJ6A MIMXRT1061DVJ6B MIMXRT1062DVL6A MIMXRT1062DVL6B MIMXRT1062DVJ6A MIMXRT1062DVJ6B MIMXRT106ADVL6A MIMXRT106ADVL6B MIMXRT106FDVL6A MIMXRT106FDVL6B MIMXRT106PDVL6A MIMXRT106PDVL6B MIMXRT106SDVL6B MIMXRT106VDVL6B MIMXRT106DDVL6B MIMXRT106CDVL6B** 

**==> picture [45 x 36] intentionally omitted <==**

**Package Information** Plastic Package 196-pin MAPBGA, 10 x 10 mm, 0.65 mm pitch 196-pin MAPBGA, 12 x 12 mm, 0.8 mm pitch 

**Ordering Information** See Table 1 on page 6 

|1.|i.MX RT1060 Introduction . . . . . . . . . . . . . . . . . . . . . . . .  1|
|---|---|
|2.|1.1.<br>Features  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  2<br>1.2.<br>Ordering information  . . . . . . . . . . . . . . . . . . . . . . .  6<br>Architectural Overview  . . . . . . . . . . . . . . . . . . . . . . . . .  12|
|3.|2.1.<br>Block diagram  . . . . . . . . . . . . . . . . . . . . . . . . . . .  12<br>Modules List  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  13<br>3.1.<br>Special signal considerations  . . . . . . . . . . . . . . .  20|
||3.2.<br>Recommended connections for unused analog<br>interfaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  22|
|4.|Electrical Characteristics . . . . . . . . . . . . . . . . . . . . . . . .  23|
||4.1.<br>Chip-Level conditions  . . . . . . . . . . . . . . . . . . . . .  23<br>4.2.<br>System power and clocks  . . . . . . . . . . . . . . . . . .  30<br>4.3.<br>I/O parameters  . . . . . . . . . . . . . . . . . . . . . . . . . .  35|
||4.4.<br>System modules  . . . . . . . . . . . . . . . . . . . . . . . . .  42<br>4.5.<br>External memory interface  . . . . . . . . . . . . . . . . .  47<br>4.6.<br>Display and graphics . . . . . . . . . . . . . . . . . . . . . .  57|
||4.7.<br>Audio . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  60|
||4.8.<br>Analog . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  63<br>4.9.<br>Communication interfaces . . . . . . . . . . . . . . . . . .  70|
||4.10. Timers  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  83|
|5.|Boot mode configuration . . . . . . . . . . . . . . . . . . . . . . . .  85<br>5.1.<br>Boot mode configuration pins  . . . . . . . . . . . . . . .  85<br>5.2.<br>Boot device interface allocation . . . . . . . . . . . . . .  85|
|6.|Package information and contact assignments . . . . . . .  90|
|7.|6.1.<br>10 x 10 mm package information  . . . . . . . . . . . .  90<br>6.2.<br>12 x 12 mm package information  . . . . . . . . . . .  102<br>Revision history . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 114|



**==> picture [128 x 48] intentionally omitted <==**

NXP reserves the right to change the production detail specifications as may be required to permit improvements in the design of its products. 

**i.MX RT1060 Introduction** 

The i.MX RT1060 is specifically useful for applications such as: 

- Industrial Human Machine Interfaces (HMI) 

- Motor Control 

- Home Appliance 

## **1.1 Features** 

The i.MX RT1060 processors are based on Arm Cortex-M7 Core Platform, which has the following features: 

- Supports single Arm Cortex-M7 Core with: 

   - 32 KB L1 Instruction Cache 

   - 32 KB L1 Data Cache 

   - Full featured Floating Point Unit (FPU) with support of the VFPv5 architecture 

   - Support the Armv7-M Thumb instruction set 

- Integrated MPU, up to 16 individual protection regions 

- Tightly coupled GPIOs, operating at the same frequency as Arm Core 

- Up to 512 KB I-TCM and D-TCM in total 

- Frequency of 600 MHz 

- Cortex M7 CoreSight™ components integration for debug 

- Frequency of the core, as per Table 10, "Operating ranges," on page 25. 

The SoC-level memory system consists of the following additional components: 

   - Boot ROM (128 KB) 

   - On-chip RAM (1 MB) 

      - 512 KB OCRAM shared between ITCM/DTCM and OCRAM 

      - Dedicate 512 KB OCRAM 

- External memory interfaces: 

   - 8/16-bit SDRAM, up to SDRAM-133/SDRAM-166 

   - 8/16-bit SLC NAND FLASH, with ECC handled in software 

   - SD/eMMC 

   - SPI NOR/NAND FLASH 

   - Parallel NOR FLASH with XIP support 

   - Two single/dual channel Quad SPI FLASH with XIP support 

- Timers and PWMs: 

   - Two General Programmable Timers (GPT) 

      - 4-channel generic 32-bit resolution timer for each 

      - Each support standard capture and compare operation 

   - Four Periodical Interrupt Timers (PIT) 

      - Generic 32-bit resolution timer 

**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

2 

NXP Semiconductors 

**i.MX RT1060 Introduction** 

   - Periodical interrupt generation 

- Four Quad Timers (QTimer) 

   - 4-channel generic 16-bit resolution timer for each 

   - Each support standard capture and compare operation 

   - Quadrature decoder integrated 

- Four FlexPWMs 

   - Up to 8 individual PWM channels per each 

   - 16-bit resolution PWM suitable for Motor Control applications 

- Four Quadrature Encoder/Decoders 

Each i.MX RT1060 processor enables the following interfaces to external devices (some of them are muxed and not available simultaneously): 

- Display Interface: 

   - Parallel RGB LCD interface 

      - Support 8/16/24 bit interface 

      - Support up to WXGA resolution 

      - Support Index color with 256 entry x 24 bit color LUT 

      - Smart LCD display with 8/16-bit MPU/8080 interface 

- Audio: 

   - S/PDIF input and output 

   - Three synchronous audio interface (SAI) modules supporting I2S, AC97, TDM, and codec/DSP interfaces 

   - MQS interface for medium quality audio via GPIO pads 

- Generic 2D graphics engine: — BitBlit 

   - Flexible image composition options—alpha, chroma key 

   - Porter-duff blending 

   - Image rotation (90[] , 180[] , 270[] ) 

   - Image size 

   - Color space conversion 

   - Multiple pixel format support (RGB, YUV444, YUV422, YUV420, YUV400) 

   - Standard 2D-DMA operation 

- Camera sensors: — Support 24-bit, 16-bit, and 8-bit CSI input 

- Connectivity: 

   - Two USB 2.0 OTG controllers with integrated PHY interfaces 

   - Two Ultra Secure Digital Host Controller (uSDHC) interfaces 

      - MMC 4.5 compliance with HS200 support up to 200 MB/sec 

**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

NXP Semiconductors 

3 

**i.MX RT1060 Introduction** 

         - SD/SDIO 3.0 compliance with 200 MHz SDR signaling to support up to 100 MB/sec – Support for SDXC (extended capacity) 

      - Two 10/100M Ethernet controller with support for IEEE1588 

      - Eight universal asynchronous receiver/transmitter (UARTs) modules 

      - Four I2C modules 

      - Four SPI modules 

      - Two FlexCAN modules 

      - One FlexCAN (with Flexible Data-Rate supported) 

      - Three FlexIO modules 

   - GPIO and Pin Multiplexing: 

      - General-purpose input/output (GPIO) modules with interrupt capability 

      - Input/output multiplexing controller (IOMUXC) to provide centralized pad control 

- The i.MX RT1060 processors integrate advanced power management unit and controllers: 

   - Full PMIC integration, including on-chip DCDC and LDO 

   - Temperature sensor with programmable trim points 

   - GPC hardware power management controller 

- The i.MX RT1060 processors support the following system debug: 

   - Arm CoreSight debug and trace architecture 

   - Trace Port Interface Unit (TPIU) to support off-chip real-time trace 

   - Cross Triggering Interface (CTI) 

   - Support for 5-pin (JTAG) and SWD debug interfaces 

- The i.MX RT1060 processors support the following analog interfaces: 

   - Two Analog-Digital-Converters (ADC), 16-channel for each, 20-channel in total 

   - Four Analog Comparators (ACMP) 

- Security functions are enabled and accelerated by the following hardware: 

   - High Assurance Boot (HAB) 

   - Data Co-Processor (DCP): 

      - AES-128, ECB, and CBC mode 

      - SHA-1 and SHA-256 

      - CRC-32 

   - Bus Encryption Engine (BEE) 

      - AES-128, ECB, and CTR mode 

      - On-the-fly QSPI Flash decryption 

   - True random number generation (TRNG) 

   - Secure Non-Volatile Storage (SNVS) 

      - Secure real-time clock (RTC) 

**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

4 

NXP Semiconductors 

**i.MX RT1060 Introduction** 

   - Zero Master Key (ZMK) 

- Secure JTAG Controller (SJC) 

## **NOTE** 

The actual feature set depends on the part numbers as described in Table 1. Functions such as display and camera interfaces, connectivity interfaces, and security features are not offered on all derivatives. 

**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

NXP Semiconductors 

5 

**i.MX RT1060 Introduction** 

## **1.2 Ordering information** 

Table 1 provides examples of orderable part numbers covered by this Data Sheet. 

**Table 1. Ordering information** 

|**Part Number**|**Features**|**Features**|**Package**|**Junction**<br>**Temperature**<br>**Tj (****C)**|
|---|---|---|---|---|
|MIMXRT1061DVJ6A<br>MIMXRT1061DVJ6B|• 600 MHz, commercial<br>grade for general purpose,<br>with MPU/FPU<br>• eDMA<br>• Boot ROM (128 KB)<br>• On-chip RAM (1 MB)<br>• SEMC<br>• GPT x2<br>• 4-channel PIT<br>• Qtimer x4<br>• PWM x4<br>• ENC x4<br>• WDOG x4<br>• No LCD/CSI/PXP<br>• SPDIF x1<br>• SAI x3<br>• MQS x1<br>• USB OTG x2<br>• eMMC 4.5/SD 3.0 x2|• Ethernet x2<br>• UART x8<br>• I2C x4<br>• FlexSPI x2<br>• CAN x2<br>• FlexCAN (with Flexible<br>Data-Rate supported)<br>• FlexIO x3<br>• 127 GPIOs (124 tightly<br>coupled)<br>• HAB/DCP/BEE<br>• TRNG<br>• SNVS<br>• SJC<br>• ADC x2<br>• ACMP x4<br>• TSC<br>• DCDC<br>• Temperature sensor<br>• GPC hardware power<br>management controller|12 x 12 mm, 0.8 mm<br>pitch, 196-pin MAPBGA|0 to +95|
|MIMXRT1061DVL6A<br>MIMXRT1061DVL6B|• 600 MHz, commercial<br>grade for general purpose,<br>with MPU/FPU<br>• eDMA<br>• Boot ROM (128 KB)<br>• On-chip RAM (1 MB)<br>• SEMC<br>• GPT x2<br>• 4-channel PIT<br>• Qtimer x4<br>• PWM x4<br>• ENC x4<br>• WDOG x4<br>• No LCD/CSI/PXP<br>• SPDIF x1<br>• SAI x3<br>• MQS x1<br>• USB OTG x2<br>• eMMC 4.5/SD 3.0 x2|• Ethernet x2<br>• UART x8<br>• I2C x4<br>• FlexSPI x2<br>• CAN x2<br>• FlexCAN (with Flexible<br>Data-Rate supported)<br>• FlexIO x3<br>• 127 GPIOs (124 tightly<br>coupled)<br>• HAB/DCP/BEE<br>• TRNG<br>• SNVS<br>• SJC<br>• ADC x2<br>• ACMP x4<br>• TSC<br>• DCDC<br>• Temperature sensor<br>• GPC hardware power<br>management controller|10 x 10 mm, 0.65 mm<br>pitch, 196-pin MAPBGA|0 to +95|



**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

6 

NXP Semiconductors 

**i.MX RT1060 Introduction** 

## **Table 1. Ordering information** 

|**Part Number**|**Features**|**Features**|**Package**|**Junction**<br>**Temperature**<br>**Tj (****C)**|
|---|---|---|---|---|
|MIMXRT1062DVJ6A<br>MIMXRT1062DVJ6B|• 600 MHz, commercial<br>grade for general purpose,<br>with MPU/FPU<br>• eDMA<br>• Boot ROM (128 KB)<br>• On-chip RAM (1 MB)<br>• SEMC<br>• GPT x2<br>• 4-channel PIT<br>• Qtimer x4<br>• PWM x4<br>• ENC x4<br>• WDOG x4<br>• LCD/CSI/PXP<br>• SPDIF x1<br>• SAI x3<br>• MQS x1<br>• USB OTG x2<br>• eMMC 4.5/SD 3.0 x2|• Ethernet x2<br>• UART x8<br>• I2C x4<br>• FlexSPI x2<br>• CAN x2<br>• FlexCAN (with Flexible<br>Data-Rate supported)<br>• FlexIO x3<br>• 127 GPIOs (124 tightly<br>coupled)<br>• HAB/DCP/BEE<br>• TRNG<br>• SNVS<br>• SJC<br>• ADC x2<br>• ACMP x4<br>• TSC<br>• DCDC<br>• Temperature sensor<br>• GPC hardware power<br>management controller|12 x 12 mm, 0.8 mm<br>pitch, 196-pin MAPBGA|0 to +95|
|MIMXRT1062DVL6A<br>MIMXRT1062DVL6B|• 600 MHz, commercial<br>grade for general purpose,<br>with MPU/FPU<br>• eDMA<br>• Boot ROM (128 KB)<br>• On-chip RAM (1 MB)<br>• SEMC<br>• GPT x2<br>• 4-channel PIT<br>• Qtimer x4<br>• PWM x4<br>• ENC x4<br>• WDOG x4<br>• LCD/CSI/PXP<br>• SPDIF x1<br>• SAI x3<br>• MQS x1<br>• USB OTG x2<br>• eMMC 4.5/SD 3.0 x2|• Ethernet x2<br>• UART x8<br>• I2C x4<br>• FlexSPI x2<br>• CAN x2<br>• FlexCAN (with Flexible<br>Data-Rate supported)<br>• FlexIO x3<br>• 127 GPIOs (124 tightly<br>coupled)<br>• HAB/DCP/BEE<br>• TRNG<br>• SNVS<br>• SJC<br>• ADC x2<br>• ACMP x4<br>• TSC<br>• DCDC<br>• Temperature sensor<br>• GPC hardware power<br>management controller|10 x 10 mm, 0.65 mm<br>pitch, 196-pin MAPBGA|0 to +95|



**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

NXP Semiconductors 

7 

**i.MX RT1060 Introduction** 

**Table 1. Ordering information** 

|**Part Number**|**Features**|**Features**|**Package**|**Junction**<br>**Temperature**<br>**Tj (****C)**|
|---|---|---|---|---|
|MIMXRT106ADVL6A<br>MIMXRT106ADVL6B|• 600 MHz, commercial<br>grade for general purpose,<br>with MPU/FPU<br>• Turnkey solution with NXP<br>VoiceSeeker AFE and<br>VoiceSpot Wake Word for<br>Alexa for IoT<br>• eDMA<br>• Boot ROM (128 KB)<br>• On-chip RAM (1 MB)<br>• SEMC<br>• GPT x2<br>• 4-channel PIT<br>• Qtimer x4<br>• PWM x4<br>• ENC x4<br>• WDOG x4<br>• LCD/CSI/PXP<br>• SPDIF x1<br>• SAI x3<br>• MQS x1<br>• USB OTG x2|• eMMC 4.5/SD 3.0 x2<br>• Ethernet x2<br>• UART x8<br>• I2C x4<br>• FlexSPI x2<br>• CAN x2<br>• FlexCAN (with Flexible<br>Data-Rate supported)<br>• FlexIO x3<br>• 127 GPIOs (124 tightly<br>coupled)<br>• HAB/DCP/BEE<br>• TRNG<br>• SNVS<br>• SJC<br>• ADC x2<br>• ACMP x4<br>• TSC<br>• DCDC<br>• Temperature sensor<br>• GPC hardware power<br>management controller|10 x 10 mm, 0.65 mm<br>pitch, 196-pin MAPBGA|0 to +95|
|MIMXRT106FDVL6A<br>MIMXRT106FDVL6B|• 600 MHz, commercial<br>grade for general purpose,<br>with MPU/FPU<br>• Turnkey solution for face<br>and emotion recognition,<br>seewww.<br>nxp.com/mcu-vision2<br>• eDMA<br>• Boot ROM (128 KB)<br>• On-chip RAM (1 MB)<br>• SEMC<br>• GPT x2<br>• 4-channel PIT<br>• Qtimer x4<br>• PWM x4<br>• ENC x4<br>• WDOG x4<br>• LCD/CSI/PXP<br>• SPDIF x1<br>• SAI x3<br>• MQS x1<br>• USB OTG x2|• eMMC 4.5/SD 3.0 x2<br>• Ethernet x2<br>• UART x8<br>• I2C x4<br>• FlexSPI x2<br>• CAN x2<br>• FlexCAN (with Flexible<br>Data-Rate supported)<br>• FlexIO x3<br>• 127 GPIOs (124 tightly<br>coupled)<br>• HAB/DCP/BEE<br>• TRNG<br>• SNVS<br>• SJC<br>• ADC x2<br>• ACMP x4<br>• TSC<br>• DCDC<br>• Temperature sensor<br>• GPC hardware power<br>management controller|10 x 10 mm, 0.65 mm<br>pitch, 196-pin MAPBGA|0 to +95|



**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

8 

NXP Semiconductors 

**i.MX RT1060 Introduction** 

## **Table 1. Ordering information** 

|**Part Number**|**Features**|**Features**|**Package**|**Junction**<br>**Temperature**<br>**Tj (****C)**|
|---|---|---|---|---|
|MIMXRT106PDVL6A|• 600 MHz, commercial<br>grade for general purpose,<br>with MPU/FPU<br>• TurnKey solution with NXP<br>VoiceSeeker AFE and<br>VoiceSpot Wake<br>• eDMA<br>• Boot ROM (128 KB)<br>• On-chip RAM (1 MB)<br>• SEMC<br>• GPT x2<br>• 4-channel PIT<br>• Qtimer x4<br>• PWM x4<br>• ENC x4<br>• WDOG x4<br>• LCD/CSI/PXP<br>• SPDIF x1<br>• SAI x3<br>• MQS x1|• USB OTG x2<br>• eMMC 4.5/SD 3.0 x2<br>• Ethernet x2<br>• UART x8<br>• I2C x4<br>• FlexSPI x2<br>• CAN x2<br>• FlexCAN (with Flexible<br>Data-Rate supported)<br>• FlexIO x3<br>• 127 GPIOs (124 tightly<br>coupled)<br>• HAB/DCP/BEE<br>• TRNG<br>• SNVS<br>• SJC<br>• ADC x2<br>• ACMP x4<br>• TSC<br>• DCDC<br>• Temperature sensor<br>• GPC hardware power<br>management controller|10 x 10 mm, 0.65 mm<br>pitch, 196-pin MAPBGA|0 to +95|



**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

NXP Semiconductors 

9 

**i.MX RT1060 Introduction** 

**Table 1. Ordering information** 

|**Part Number**|**Features**|**Features**|**Package**|**Junction**<br>**Temperature**<br>**Tj (****C)**|
|---|---|---|---|---|
|MIMXRT106SDVL6B|• 600 MHz, commercial<br>grade for general purpose,<br>with MPU/FPU<br>• Turnkey solution for local<br>voice (phoneme based)<br>recognition, see<br>www.nxp.com/mcu-local2<br>• eDMA<br>• Boot ROM (128 KB)<br>• On-chip RAM (1 MB)<br>• SEMC<br>• GPT x2<br>• 4-channel PIT<br>• Qtimer x4<br>• PWM x4<br>• ENC x4<br>• WDOG x4<br>• LCD/CSI/PXP<br>• SPDIF x1<br>• SAI x3<br>• MQS x1<br>• USB OTG x2|• eMMC 4.5/SD 3.0 x2<br>• Ethernet x2<br>• UART x8<br>• I2C x4<br>• FlexSPI x2<br>• CAN x2<br>• FlexCAN (with Flexible<br>Data-Rate supported)<br>• FlexIO x3<br>• 127 GPIOs (124 tightly<br>coupled)<br>• HAB/DCP/BEE<br>• TRNG<br>• SNVS<br>• SJC<br>• ADC x2<br>• ACMP x4<br>• TSC<br>• DCDC<br>• Temperature sensor<br>• GPC hardware power<br>management controller|10 x 10 mm, 0.65 mm<br>pitch, 196-pin MAPBGA|0 to +95|
|MIMXRT106VDVL6B<br>MIMXRT106CDVL6B<br>MIMXRT106DDVL6B<br>MIMXRT106PDVL6B|• 600 MHz, commercial<br>• grade for general purpose,<br>• with MPU/FPU<br>• eDMA<br>• Boot ROM (128 KB)<br>• On-chip RAM (1 MB)<br>• SEMC<br>• GPT x2<br>• 4-channel PIT<br>• Qtimer x4<br>• PWM x4<br>• ENC x4<br>• WDOG x4<br>• LCD/CSI/PXP<br>• SPDIF x1<br>• SAI x3<br>• MQS x1<br>• USB OTG x2<br>• eMMC 4.5/SD 3.0 x2|• Ethernet x2<br>• UART x8<br>• I2C x4<br>• FlexSPI x2<br>• CAN x2<br>• FlexCAN (with Flexible<br>• Data-Rate supported)<br>• FlexIO x3<br>• 127 GPIOs (124 tightly<br>• coupled)<br>• HAB/DCP/BEE<br>• TRNG<br>• SNVS<br>• SJC<br>• ADC x2<br>• ACMP x4<br>• TSC<br>• DCDC<br>• Temperature sensor<br>• GPC hardware power<br>management controller|10 x 10 mm, 0.65 mm<br>pitch, 196-pin MAPBGA|0 to +95|



Figure 1 describes the part number nomenclature so that characteristics of a specific part number can be identified (for example, cores, frequency, temperature grade, fuse options, and silicon revision). The primary characteristic which describes which data sheet applies to a specific part is the temperature grade (junction) field. 

**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

10 

NXP Semiconductors 

**i.MX RT1060 Introduction** 

Ensure to have the proper data sheet for specific part by verifying the temperature grade (junction) field and matching it to the proper data sheet. If there are any questions, visit the web page nxp.com/IMXRT or contact an NXP representative for details. 

**==> picture [494 x 372] intentionally omitted <==**

**----- Start of picture text -----**<br>
M IMX XX @ ## % + VV $ A<br>Qualification level M Silicon rev A<br>Prototype samples P A0 A<br>Mass production M A1 B<br>Special S<br>Core frequency $<br>Part # series XX 400 MHz 4<br>i.MX RT RT 500 MHz 5<br>600 MHz 6<br>Family @<br>First generation RT family 1 Package type VV<br>Reserved 2-8 225MAPBGA, 13 x 13 mm, 0.8 mm pitch VN<br>196MAPBGA, 12 x 12 mm, 0.8 mm pitch VJ<br>Sub-family ## 196MAPBGA, 10 x 10 mm, 0.65 mm pitch VL<br>RT101x 01<br>169MAPBGA, 11 x 11 mm, 0.8 mm pitch JM<br>RT102x 02<br>169MAPBGA, 9 x 9 mm, 0.65 mm pitch FP<br>RT104x 04<br>144LQFP, 20 x 20 mm, 0.5 mm pitch AG<br>RT105x 05<br>100LQFP, 14 x 14 mm, 0.5 mm pitch AF<br>RT106x 06<br>80LQFP, 12 x 12 mm, 0.5 mm pitch AE<br>Tie % Temperature (Tj) +<br>Standard feature 1 Consumer: 0 to +95°C D<br>Full feature 2 Industrial: -40 to +105°C C<br>4MB flash SIP 4 Extended industrial: -40 to +125°C X<br>Enhanced feature 5<br>Far field AFE A<br>Facial recognition F<br>VoiceSeeker + VIT V<br>VoiceSeeker + Cyberon C<br>VoiceSeeker + VoiceSpot for Alexa P<br>VoiceSeeker + Conversa D<br>Local voice control (text input models) S<br>**----- End of picture text -----**<br>


**Figure 1. Part number nomenclature—i.MX RT10XX family** 

**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

NXP Semiconductors 

11 

**Architectural Overview** 

## **2 Architectural Overview** 

The following subsections provide an architectural overview of the i.MX RT1060 processor system. 

## **2.1 Block diagram** 

Figure 2 shows the functional modules in the i.MX RT1060 processor system[1] . 

**==> picture [504 x 467] intentionally omitted <==**

**----- Start of picture text -----**<br>
System control CPU platform Connectivity<br>Secure JTAG Arm Cortex-M7 eMMC 4.5/SD 3.0 x2<br>PLL/OSC 32 kB I-cache 32 kB D-cache<br>UART x8<br>RTC and Reset FPU MPU NVIC<br>8 x 8 Keypad<br>Enhanced DMA Up to 512 kB TCM<br>I2C x4<br>IOMUX High-speed GPIO FLEXIO3<br>GPIO 6/7/8/9<br>SPI x4<br>GP Timer x2<br>Multimedia<br>Quadrature ENC x4 GPIO<br>8/16/24-bit Parallel CSI<br>QuadTimer I2S/SAI x3<br>(4-Channel) x4<br>24-bit Parallel LCD<br>FlexPWM S/PDIF Tx/Rx<br>(4-Channel) x4<br>PXP FlexCAN x2<br>Watch Dog x4 2D graphics acceleration<br>resize, CSC, overlay, rotation<br>USB 2.0 OTG with PHY x2<br>Internal memory<br>512 kB OCRAM External memory 10/100 ENET<br>with IEEE 1588 x1<br>128 kB ROM FlexSPI x2 (dual-channel QuadSPI<br>NAND and NOR, Octal Flash, and RAM) FLEXIO1/FLEXIO2<br>Power management<br>ADC<br>DCDC External Memory Controller<br>8-bit/16-bit SDRAM<br>Parallel NOR FLASH ADC x2 (20-channel)<br>LDO<br>NAND FLASH<br>PSRAM<br>Temp monitor ACMP x4<br>Security<br>Ciphers and RNG Secure RTC eFuse HAB<br>aaa-055232<br>**----- End of picture text -----**<br>


. 

**Figure 2. i.MX RT1060 system block diagram** 

> 1. Some modules shown in this block diagram are not offered on all derivatives. See Table 1 for details. 

**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

12 

NXP Semiconductors 

**Modules List** 

## **3 Modules List** 

The i.MX RT1060 processors contain a variety of digital and analog modules. Table 2 describes these modules in alphabetical order. 

**Table 2. i.MX RT1060 modules list** 

|**Block Mnemonic**|**Block Name**|**Subsystem**|**Brief Description**|
|---|---|---|---|
|ACMP1<br>ACMP2<br>ACMP3<br>ACMP4|Analog Comparator|Analog|The comparator (CMP) provides a circuit for comparing<br>two analog input voltages. The comparator circuit is<br>designed to operate across the full range of the supply<br>voltage (rail-to-rail operation).|
|ADC1<br>ADC2|Analog to Digital<br>Converter|Analog|The ADC is a 12-bit general purpose analog to digital<br>converter.|
|AOI|And-Or-Inverter|Cross Trigger|The AOI provides a universal boolean function<br>generator using a four team sum of products expression<br>with each product term containing true or complement<br>values of the four selected inputs (A, B, C, D).|
|Arm|Arm Platform|Arm|The Arm Core Platform includes one Cortex-M7 core. It<br>includes associated sub-blocks, such as Nested<br>Vectored Interrupt Controller (NVIC), Floating-Point<br>Unit (FPU), Memory Protection Unit (MPU), and<br>CoreSight debug modules.|
|BEE|Bus Encryption Engine|Security|On-The-Fly FlexSPI Flash Decryption|
|CCM<br>GPC<br>SRC|Clock Control Module,<br>General Power<br>Controller, System Reset<br>Controller|Clocks, Resets, and<br>Power Control|These modules are responsible for clock and reset<br>distribution in the system, and also for the system<br>power management.|
|CSI|Parallel CSI|Multimedia<br>Peripherals|The CSI IP provides parallel CSI standard camera<br>interface port. The CSI parallel data ports are up to 24<br>bits. It is designed to support 24-bit RGB888/YUV444,<br>CCIR656 video interface, 8-bit YCbCr, YUV or RGB,<br>and 8-bit/10-bit/16-bit Bayer data input.|
|CSU|Central Security Unit|Security|The Central Security Unit (CSU) is responsible for<br>setting comprehensive security policy within the i.MX<br>RT1060 platform.|
|DAP|Debug Access Port|System Control<br>Peripherals|The DAP provides real-time access for the debugger<br>without halting the core to:<br>• System memory and peripheral registers<br>• All debug configuration registers<br>The DAP also provides debugger access to JTAG scan<br>chains. The DAP module is internal to the Cortex-M7<br>Core Platform.|



**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

NXP Semiconductors 

13 

**Modules List** 

**Table 2. i.MX RT1060 modules list (continued)** 

|**Block Mnemonic**|**Block Name**|**Subsystem**|**Brief Description**|
|---|---|---|---|
|DCDC|DCDC Converter|Analog|The DCDC module is used for generating power supply<br>for core logic. Main features are:<br>• Adjustable high efficiency regulator<br>• Supports 3.3 V input voltage<br>• Supports nominal run and low power standby modes<br>• Supports at 0.9 ~ 1.3 V output in run mode<br>• Supports at 0.9 ~ 1.0 V output in standby mode<br>• Over current and over voltage detection|
|eDMA|enhanced Direct Memory<br>Access|System Control<br>Peripherals|There is an enhanced DMA (eDMA) engine and two<br>DMA_MUX.<br>• The eDMA is a 32 channel DMA engine, which is<br>capable of performing complex data transfers with<br>minimal intervention from a host processor.<br>• The DMA_MUX is capable of multiplexing up to 128<br>DMA request sources to the 32 DMA channels of<br>eDMA.|
|ENC|Quadrature<br>Encoder/Decoder|Timer Peripherals|The enhanced quadrature encoder/decoder module<br>provides interfacing capability to position/speed<br>sensors. There are five input signals: PHASEA,<br>PHASEB, INDEX, TRIGGER, and HOME. This module<br>is used to decode shaft position, revolution count, and<br>speed.|
|ENET|Ethernet Controller|Connectivity<br>Peripherals|The Ethernet Media Access Controller (MAC) is<br>designed to support 10/100 Mbit/s Ethernet/IEEE 802.3<br>networks. An external transceiver interface and<br>transceiver function are required to complete the<br>interface to the media. The module has dedicated<br>hardware to support the IEEE 1588 standard. See the<br>ENET chapter of the reference manual for details.|
|EWM|External Watchdog<br>Monitor|Timer Peripherals|The EWM modules is designed to monitor external<br>circuits, as well as the software flow. This provides a<br>back-up mechanism to the internal WDOG that can<br>reset the system. The EWM differs from the internal<br>WDOG in that it does not reset the system. The EWM,<br>if allowed to time-out, provides an independent trigger<br>pin that when asserted resets or places an external<br>circuit into a safe mode.|
|FLEXCAN1<br>FLEXCAN2|Flexible Controller Area<br>Network|Connectivity<br>Peripherals|The CAN protocol was primarily, but not only, designed<br>to be used as a vehicle serial data bus, meeting the<br>specific requirements of this field: real-time processing,<br>reliable operation in the Electromagnetic interference<br>(EMI) environment of a vehicle, cost-effectiveness and<br>required bandwidth. The FlexCAN module is a full<br>implementation of the CAN protocol specification,<br>Version 2.0 B, which supports both standard and<br>extended message frames.|



**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

14 

NXP Semiconductors 

**Modules List** 

**Table 2. i.MX RT1060 modules list (continued)** 

|**Block Mnemonic**|**Block Name**|**Subsystem**|**Brief Description**|
|---|---|---|---|
|FLEXCAN (FD)|Flexible Controller Area<br>Network|Connectivity<br>Peripherals|The CAN with Flexible Data-Rate protocol and the CAN<br>2.0 version B protocol supports both standard and<br>extended message frames, both of them have long<br>payloads up to 64 bytes transferred at faster rates up to<br>8 Mbps.|
|FlexIO1<br>FlexIO2<br>FlexIO3|Flexible Input/output|Connectivity and<br>Communications|The FlexIO is capable of supporting a wide range of<br>protocols including, but not limited to: UART, I2C, SPI,<br>I2S, camera interface, display interface, PWM<br>waveform generation, etc. The module can remain<br>functional when the chip is in a low power mode<br>provided the clock it is using remain active.|
|FlexPWM1<br>FlexPWM2<br>FlexPWM3<br>FlexPWM4|Pulse Width Modulation|Timer Peripherals|The pulse-width modulator (PWM) contains four PWM<br>sub-modules, each of which is set up to control a single<br>half-bridge power stage. Fault channel support is<br>provided. The PWM module can generate various<br>switching patterns, including highly sophisticated<br>waveforms.|
|FlexRAM|RAM|Memories|The i.MX RT1060 has 1 MB of on-chip RAM which<br>could be flexible allocated to I-TCM, D-TCM, and<br>on-chip RAM (OCRAM) in a 32 KB granularity. The<br>FlexRAM is the manager of the on-chip RAM array.<br>Major functions of this blocks are: interfacing to I-TCM<br>and D-TCM of Arm core and OCRAM controller;<br>dynamic RAM arrays allocation for I-TCM, D-TCM, and<br>OCRAM.|
|FlexSPI1<br>FlexSPI2|Quad Serial Peripheral<br>Interface|Connectivity and<br>Communications|FlexSPI acts as an interface to one or two external<br>serial flash devices, each with up to four bidirectional<br>data lines.|
|GPIO1<br>GPIO2<br>GPIO3<br>GPIO4<br>GPIO5|General Purpose I/O<br>Modules|System Control<br>Peripherals|Used for general purpose input/output to external ICs.<br>Each GPIO module supports up to 32 bits of I/O.|
|GPT1<br>GPT2|General Purpose Timer|Timer Peripherals|Each GPT is a 32-bit “free-running” or “set and forget”<br>mode timer with programmable prescaler and compare<br>and capture register. A timer counter value can be<br>captured using an external event and can be configured<br>to trigger a capture event on either the leading or trailing<br>edges of an input pulse. When the timer is configured to<br>operate in “set and forget” mode, it is capable of<br>providing precise interrupts at regular intervals with<br>minimal processor intervention. The counter has output<br>compare logic to provide the status and interrupt at<br>comparison. This timer can be configured to run either<br>on an external clock or on an internal clock.|



**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

NXP Semiconductors 

15 

**Modules List** 

**Table 2. i.MX RT1060 modules list (continued)** 

|**Block Mnemonic**|**Block Name**|**Subsystem**|**Brief Description**|
|---|---|---|---|
|KPP|Keypad Port|Human Machine<br>Interfaces|The KPP is a 16-bit peripheral that can be used as a<br>keypad matrix interface or as general purpose<br>input/output (I/O). It supports 8 x 8 external key pad<br>matrix. Main features are:<br>• Multiple-key detection<br>• Long key-press detection<br>• Standby key-press detection<br>• Supports a 2-point and 3-point contact key matrix|
|LCDIF|LCD interface|Multimedia<br>Peripherals|The LCDIF is a general purpose display controller used<br>to drive a wide range of display devices varying in size<br>and capabilities. The LCDIF is designed to support<br>dumb (synchronous 24-bit Parallel RGB interface) and<br>smart (asynchronous parallel MPU interface) LCD<br>devices.|
|LPI2C1<br>LPI2C2<br>LPI2C3<br>LPI2C4|Low Power<br>Inter-integrated Circuit|Connectivity and<br>Communications|The LPI2C is a low power Inter-Integrated Circuit (I2C)<br>module that supports an efficient interface to an I2C bus<br>as a master.<br>The I2C provides a method of communication between<br>a number of external devices. More detailed<br>information, seeSection 4.9.2, LPI2C module timing<br>parameters.|
|LPSPI1<br>LPSPI2<br>LPSPI3<br>LPSPI4|Low Power Serial<br>Peripheral Interface|Connectivity and<br>Communications|The LPSPI is a low power Serial Peripheral Interface<br>(SPI) module that support an efficient interface to an<br>SPI bus as a master and/or a slave.<br>• It can continue operating while the chip is in stop<br>modes, if an appropriate clock is available<br>• Designed for low CPU overhead, with DMA off<br>loading of FIFO register access|
|LPUART1<br>LPUART2<br>LPUART3<br>LPUART4<br>LPUART5<br>LPUART6<br>LPUART7<br>LPUART8|UART Interface|Connectivity<br>Peripherals|Each of the UART modules support the following serial<br>data transmit/receive protocols and configurations:<br>• 7- or 8-bit data words, 1 or 2 stop bits, programmable<br>parity (even, odd or none)<br>• Programmable baud rates up to 20 Mbps.|
|MQS|Medium Quality Sound|Multimedia<br>Peripherals|MQS is used to generate 2-channel medium quality<br>PWM-like audio via two standard digital GPIO pins.|
|PXP|Pixel Processing Pipeline|Multimedia<br>Peripherals|A high-performance pixel processor capable of 1<br>pixel/clock performance for combined operations, such<br>as color-space conversion, alpha blending, and<br>rotation. The PXP is enhanced<br>with features specifically for gray scale applications. In<br>addition, the PXP supports traditional pixel/frame<br>processing paths for still-image and video processing<br>applications.|



**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

16 

NXP Semiconductors 

**Modules List** 

**Table 2. i.MX RT1060 modules list (continued)** 

|**Block Mnemonic**|**Block Name**|**Subsystem**|**Brief Description**|
|---|---|---|---|
|QuadTimer1<br>QuadTimer2<br>QuadTimer3<br>QuadTimer4|QuadTimer|Timer Peripherals|The quad-timer provides four time channels with a<br>variety of controls affecting both individual and<br>multi-channel features.Specific features include<br>up/down count, cascading of counters, programmable<br>module, count once/repeated, counter preload,<br>compare registers with preload, shared use of input<br>signals, prescaler controls, independent<br>capture/compare, fault input control, programmable<br>input filters, and multi-channel synchronization.|
|ROMCP|ROM Controller with<br>Patch|Memories and<br>Memory Controllers|The ROMCP acts as an interface between the Arm<br>advanced high-performance bus and the ROM. The<br>on-chip ROM is only used by the Cortex-M7 core during<br>boot up. Size of the ROM is 96 KB.|
|RTC OSC|Real Time Clock<br>Oscillator|Clock Sources and<br>Control|The RTC OSC provides the clock source for the<br>Real-Time Clock module. The RTC OSC module, in<br>conjunction with an external crystal, generates a 32.768<br>kHz reference clock for the RTC.|
|RTWDOG|Watch Dog|Timer Peripherals|The RTWDG module is a high reliability independent<br>timer that is available for system to use. It provides a<br>safety feature to ensure software is executing as<br>planned and the CPU is not stuck in an infinite loop or<br>executing unintended code. If the WDOG module is not<br>serviced (refreshed) within a certain period, it resets the<br>MCU. Windowed refresh mode is supported as well.|
|SAI1<br>SAI2<br>SAI3|Synchronous Audio<br>Interface|Multimedia<br>Peripherals|The SAI module provides a synchronous audio<br>interface (SAI) that supports full duplex serial interfaces<br>with frame synchronization, such as I2S, AC97, TDM,<br>and codec/DSP interfaces.|
|SA-TRNG|Standalone True Random<br>Number Generator|Security|The SA-TRNG is hardware accelerator that generates<br>a 512-bit entropy as needed by an entropy consuming<br>module or by other post processing functions.|
|SEMC|Smart External Memory<br>Controller|Memory and<br>Memory Controller|The SEMC is a multi-standard memory controller<br>optimized for both high-performance and low pin-count.<br>It can support multiple external memories in the same<br>application with shared address and data pins. The<br>interface supported includes SDRAM, NOR Flash,<br>SRAM, and NAND Flash, as well as 8080 display<br>interface.|



**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

NXP Semiconductors 

17 

## **Modules List** 

**Table 2. i.MX RT1060 modules list (continued)** 

|**Block Mnemonic**|**Block Name**|**Subsystem**|**Brief Description**|
|---|---|---|---|
|SJC|System JTAG Controller|System Control<br>Peripherals|The SJC provides JTAG interface, which complies with<br>JTAG TAP standards, to internal logic. The i.MX<br>RT1060 processors use JTAG port for production,<br>testing, and system debugging. In addition, the SJC<br>provides BSR (Boundary Scan Register) standard<br>support, which complies with IEEE 1149.1 and IEEE<br>1149.6 standards.<br>The JTAG port is accessible during platform initial<br>laboratory bring-up, for manufacturing tests and<br>troubleshooting, as well as for software debugging by<br>authorized entities. The i.MX RT1060 SJC incorporates<br>three security modes for protecting against<br>unauthorized accesses. Modes are selected through<br>eFUSE configuration.|
|SNVS|Secure Non-Volatile<br>Storage|Security|Secure Non-Volatile Storage, including Secure Real<br>Time Clock, Security State Machine, Master Key<br>Control, Violation, and reporting.|
|SPDIF|Sony Philips Digital<br>Interconnect Format|Multimedia<br>Peripherals|A standard audio file transfer format, developed jointly<br>by the Sony and Phillips corporations. Has Transmitter<br>and Receiver functionality.|
|Temp Monitor|Temperature Monitor|Analog|The temperature sensor implements a temperature<br>sensor/conversion function based on a<br>temperature-dependent voltage to time conversion.|
|TSC|Touch Screen|Human Machine<br>Interfaces|With touch controller to support 4-wire and 5-wire<br>resistive touch panel.|
|USBO2|Universal Serial Bus 2.0|Connectivity<br>Peripherals|USBO2 (USB OTG1 and USB OTG2) contains:<br>• Two high-speed OTG 2.0 modules with integrated<br>HS USB PHYs<br>• Support eight Transmit (TX) and eight Receive (Rx)<br>endpoints, including endpoint 0|



**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

18 

NXP Semiconductors 

**Modules List** 

**Table 2. i.MX RT1060 modules list (continued)** 

|**Block Mnemonic**|**Block Name**|**Subsystem**|**Brief Description**|
|---|---|---|---|
|uSDHC1<br>uSDHC2|SD/MMC and SDXC<br>Enhanced Multi-Media<br>Card / Secure Digital Host<br>Controller|Connectivity<br>Peripherals|i.MX RT1060 specific SoC characteristics:<br>All four MMC/SD/SDIO controller IPs are identical and<br>are based on the uSDHC IP. They are:<br>• Fully compliant with MMC command/response sets<br>and Physical Layer as defined in the Multimedia<br>Card System Specification, v4.5/4.2/4.3/4.4/4.41/<br>including high-capacity (size > 2 GB) cards HC<br>MMC.<br>• Fully compliant with SD command/response sets<br>and Physical Layer as defined in the SD Memory<br>Card Specifications, v3.0 including high-capacity<br>SDXC cards up to 2 TB.<br>• Fully compliant with SDIO command/response sets<br>and interrupt/read-wait mode as defined in the SDIO<br>Card Specification, Part E1, v3.0<br>Two ports support:<br>• 1-bit or 4-bit transfer mode specifications for SD and<br>SDIO cards up to UHS-I SDR104 mode (104 MB/s<br>max)<br>• 1-bit, 4-bit, or 8-bit transfer mode specifications for<br>MMC cards up to 52 MHz in both SDR and DDR<br>modes (104 MB/s max)<br>• 4-bit or 8-bit transfer mode specifications for eMMC<br>chips up to 200 MHz in HS200 mode (200 MB/s max)|
|WDOG1<br>WDOG2|Watch Dog|Timer Peripherals|The watchdog (WDOG) Timer supports two comparison<br>points during each counting period. Each of the<br>comparison points is configurable to evoke an interrupt<br>to the Arm core, and a second point evokes an external<br>event on the WDOG line.|
|XBAR|Cross BAR|Cross Trigger|Each crossbar switch is an array of muxes with shared<br>inputs. Each mux output provides one output of the<br>crossbar. The number of inputs and the number of<br>muxes/outputs are user configurable and registers are<br>provided to select which of the shared inputs are routed<br>to each output.|



**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

NXP Semiconductors 

19 

**Modules List** 

## **3.1 Special signal considerations** 

Table 3 lists special signal considerations for the i.MX RT1060 processors. The signal names are listed in alphabetical order. 

The package contact assignments can be found in Section 6, Package information and contact assignments.” Signal descriptions are provided in the _i.MX RT1060 Reference Manual_ (IMXRT1060RM). 

## **Table 3. Special signal considerations** 

|**Signal Name**|**Remarks**|
|---|---|
|CCM_CLK1_P/<br>CCM_CLK1_N|One general purpose differential high speed clock Input/output (LVDS I/O) is provided.<br>It can be used:<br>• To feed external reference clock to the PLLs and further to the modules inside SoC.<br>• To output internal SoC clock to be used outside the SoC as either reference clock or as a<br>functional clock for peripherals.<br>See the_i.MX RT1060 Reference Manual_(IMXRT1060RM) for details on the respective clock trees.<br>Alternatively one may use single ended signal to drive CLK1_P input. In this case corresponding<br>CLK1_N input should be tied to the constant voltage level equal 1/2 of the input signal swing.<br>Termination should be provided in case of high frequency signals.<br>After initialization, the CLK1 input/output can be disabled (if not used). If unused either or both of<br>the CLK1_N/P pairs may remain unconnected.|
|DCDC_PSWITCH|PAD is in DCDC_IN domain and connected the ground to bypass DCDC.<br>To enable DCDC function, assert to DCDC_IN with at least 1ms delay for DCDC_IN rising edge.|
|RTC_XTALI/RTC_XTALO|If the user wishes to configure RTC_XTALI and RTC_XTALO as an RTC oscillator, a 32.768 kHz<br>crystal, (100 kESR, 10 pF load) should be connected between RTC_XTALI and RTC_XTALO.<br>Keep in mind the capacitors implemented on either side of the crystal are about twice the crystal<br>load capacitor. To hit the exact oscillation frequency, the board capacitors need to be reduced to<br>account for board and chip parasitics. The integrated oscillation amplifier is self biasing, but<br>relatively weak. Care must be taken to limit parasitic leakage from RTC_XTALI and RTC_XTALO<br>to either power or ground (>100 M). This will debias the amplifier and cause a reduction of startup<br>margin. Typically RTC_XTALI and RTC_XTALO should bias to approximately 0.5 V.<br>If it is desired to feed an external low frequency clock into RTC_XTALI the RTC_XTALO pin must<br>remain unconnected or driven with a complimentary signal. The logic level of this forcing clock<br>should not exceed VDD_SNVS_CAP level and the frequency should be <100 kHz under typical<br>conditions.<br>In case when high accuracy real time clock are not required system may use internal low frequency<br>ring oscillator. It is recommended to connect RTC_XTALI to GND and keep RTC_XTALO<br>unconnected.|
|XTALI/XTALO|A 24.0 MHz crystal should be connected between XTALI and XTALO.<br>The crystal must be rated for a maximum drive level of 250W. An ESR (equivalent series<br>resistance) of typical 80is recommended. NXP SDK software requires 24 MHz on<br>XTALI/XTALO.<br>The crystal can be eliminated if an external 24 MHz oscillator is available in the system. In this<br>case, XTALO must be directly driven by the external oscillator and XTALI mounted with 18 pF<br>capacitor. The logic level of this forcing clock cannot exceed NVCC_PLL level.<br>If this clock is used as a reference for USB, then there are strict frequency tolerance and jitter<br>requirements. See OSC24M chapter and relevant interface specifications chapters for details.|
|GPANAIO|This signal is reserved for NXP manufacturing use only. This output must remain unconnected.|



**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

20 

NXP Semiconductors 

**Modules List** 

## **Table 3. Special signal considerations (continued)** 

||**Table 3. Special signal considerations (continued)**|
|---|---|
|**Signal Name**|**Remarks**|
|JTAGnnnn_|The JTAG interface is summarized inTable 4. Use of external resistors is unnecessary. However,<br>if external resistors are used, the user must ensure that the on-chip pull-up/down configuration is<br>followed. For example, do not use an external pull down on an input that has on-chip pull-up.|
||JTAG_TDO is configured with a keeper circuit such that the non-connected condition is eliminated<br>if an external pull resistor is not present. An external pull resistor on JTAG_TDO is detrimental and<br>should be avoided.|
||JTAG_MOD is referenced as SJC_MOD in the i.MX RT1060 reference manual (IMXRT1060RM).<br>Both names refer to the same signal. JTAG_MOD must be externally connected to GND for normal<br>operation. Termination to GND through an external pull-down resistor (such as 1 k) is allowed.<br>JTAG_MOD set to hi configures the JTAG interface to mode compliant with IEEE1149.1 standard.<br>JTAG_MOD set to low configures the JTAG interface for common SW debug adding all the system<br>TAPs to the chain.<br>**Note**:For JTAG_TRSTB pin, it is recommended to reserve<br>an external pull down resistor. keep this pull-down resistor on<br>production and remove it on debugging. If users want to use<br>other function on this pin (such as GPIO, Timer,etc), it is<br>recommended to switch JTAG_TCK and JTAG_TMS first,<br>then switch the setting of JTAG_TRSTB.|
|NC|These signals are No Connect (NC) and should be disconnected by the user.|
|POR_B|This cold reset negative logic input resets all modules and logic in the IC.<br>May be used in addition to internally generated power on reset signal (logical AND, both internal<br>and external signals are considered active low).|
|ONOFF|ONOFF can be configured in debounce, off to on time, and max time-out configurations. The<br>debounce and off to on time configurations supports 0, 50, 100 and 500 ms. Debounce is used to<br>generate the power off interrupt. While in the ON state, if ONOFF button is pressed longer than the<br>debounce time, the power off interrupt is generated. Off to on time supports the time it takes to<br>request power on after a configured button press time has been reached. While in the OFF state,<br>if ONOFF button is pressed longer than the off to on time, the state will transition from OFF to ON.<br>Max time-out configuration supports 5, 10, 15 seconds and disable. Max time-out configuration<br>supports the time it takes to request power down after ONOFF button has been pressed for the<br>defined time.|
|TEST_MODE|TEST_MODE is for NXP factory use. The user can leave this signal floating or tie it to ground.|
|WAKEUP|A GPIO powered by SNVS domain power supply which can be configured as wakeup source in<br>SNVS mode.|



## **Table 4. JTAG Controller interface summary** 

|**JTAG**|**I/O Type**|**On-chip Termination**|
|---|---|---|
|JTAG_TCK|Input|100 kpull-down|
|JTAG_TMS|Input|47 kpull-up|
|JTAG_TDI|Input|47 kpull-up|
|JTAG_TDO|3-state output|Keeper|



**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

NXP Semiconductors 

21 

## **Modules List** 

**Table 4. JTAG Controller interface summary (continued)** 

|**JTAG**|**I/O Type**|**On-chip Termination**|
|---|---|---|
|JTAG_TRSTB|Input|47 kpull-up|
|JTAG_MOD|Input|100 kpull-down|



## **3.2 Recommended connections for unused analog interfaces** 

Table 5 shows the recommended connections for unused analog interfaces. 

**Table 5. Recommended connections for unused analog interfaces** 

|**Module**|**Pad Name**|**Recommendations**<br>**if Unused**|
|---|---|---|
|CCM|CCM_CLK1_N, CCM_CLK1_P|Not connected|
|USB|USB_OTG1_CHD_B, USB_OTG1_DN, USB_OTG1_DP, USB_OTG1_VBUS,<br>USB_OTG2_DN, USB_OTG2_DP, USB_OTG2_VBUS|Not connected|
|ADC|VDDA_ADC_3P3|VDDA_ADC_3P3<br>must be powered<br>even if the ADC is<br>not used.|



**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

22 

NXP Semiconductors 

**Electrical Characteristics** 

## **4 Electrical Characteristics** 

This section provides the device and module-level electrical characteristics for the i.MX RT1060 processors. 

## **4.1 Chip-Level conditions** 

This section provides the device-level electrical characteristics for the IC. See Table 6 for a quick reference to the individual tables and sections. 

**Table 6. i.MX RT1060 chip-Level conditions** 

|**For these characteristics**|**Topic appears**|
|---|---|
|Absolute maximum ratings|on page 23|
|Thermal resistance|on page 24|
|Operating ranges|on page 25|
|External clock sources|on page 26|
|Maximum supply currents|on page 27|
|Low power mode supply currents|on page 29|
|USB PHY current consumption|on page 29|



## **4.1.1 Absolute maximum ratings** 

## **CAUTION** 

Stress beyond those listed under Table 7 may cause permanent damage to the device. These are stress ratings only. Functional operation of the device at these or any other conditions beyond those indicated under “recommended operating conditions” is not implied. Exposure to absolute-maximum-rated conditions for extended periods may affect device reliability. 

Table 7 shows the absolute maximum operating ratings. 

**Table 7. Absolute maximum ratings** 

|**Parameter Description**|**Symbol**|**Min**|**Max**|**Unit**|
|---|---|---|---|---|
|Core supplies input voltage|VDD_SOC_IN|-0.3|1.6|V|
|VDD_HIGH_IN supply voltage|VDD_HIGH_IN|-0.3|3.7|V|
|Power for DCDC|DCDC_IN|-0.3|3.6|V|
|Supply input voltage to Secure Non-Volatile Storage<br>and Real Time Clock|VDD_SNVS_IN|-0.3|3.6|V|
|USB VBUS supply|USB_OTG1_VBUS<br>USB_OTG2_VBUS|—|5.5|V|
|Supply for 12-bit ADC|VDDA_ADC|-0.3|3.6|V|



**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

NXP Semiconductors 

23 

## **Electrical Characteristics** 

## **Table 7. Absolute maximum ratings (continued)** 

|IO supply for GPIO in SDIO1 bank (3.3 V mode)|NVCC_SD0|-0.3|3.6|V|
|---|---|---|---|---|
|IO supply for GPIO in SDIO1 bank (1.8 V mode)||-0.3|1.95|V|
|IO supply for GPIO in SDIO2 bank (3.3 V mode)|NVCC_SD1|-0.3|3.6|V|
|IO supply for GPIO in SDIO2 bank (1.8 V mode)||-0.3|1.95|V|
|IO supply for GPIO in EMC bank (3.3 V mode)|NVCC_EMC|-0.3|3.6|V|
|IO supply for GPIO in EMC bank (1.8 V mode)||-0.3|1.95|V|
|ESD damage Immunity:<br>Human Body Model (HBM)<br>Charge Device Model (CDM)|Vesd|—<br>—|1000<br>500|V|
|Input/Output Voltage range|Vin/Vout|-0.5|OVDD + 0.31|V|
|Storage Temperature range|TSTORAGE|-40|150|oC|



1 OVDD is the I/O supply voltage. 

## **4.1.2 Thermal resistance** 

## **4.1.2.1 10 x 10 MM thermal resistance** 

Table 9 shows the 10 x 10 MM package thermal resistance data. 

## **Table 8. 10 x 10 MM thermal resistance data** 

|**Rating**|**Board type1**|**Symbol**|**Value**|**Unit**|
|---|---|---|---|---|
|Junction to Ambient<br>Thermal resistance2|JESD51-9, 2S2P|RJA|40.8|oC/W|
|Junction to Package Top<br>Thermal resistance2|JESD51-9, 2S2P|JT|0.5|oC/W|
|Junction to Case Thermal Resistance3|JESD51-9, 1S|RJC|16.8|oC/W|



1 Thermal test board meets JEDEC specification for this package (JESD51-9). 

2 Determined in accordance to JEDEC JESD51-2A natural convection environment. Thermal resistance data in this report is solely for a thermal performance comparison of one package to another in a standardized specified environment. It is not meant to predict the performance of a package in an application-specific environment. 

3 Junction-to-Case thermal resistance determined using an isothermal cold plate. Case temperature refers to the mold surface temperature at eh package top side dead Centre. 

**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

24 

NXP Semiconductors 

**Electrical Characteristics** 

## **4.1.2.2 12 x 12 MM thermal resistance** 

## Table 9 shows the 12 x 12 MM package thermal resistance data. 

## **Table 9. 12 x 12 MM thermal resistance data** 

|**Rating**|**Board type1**|**Symbol**|**Value**|**Unit**|
|---|---|---|---|---|
|Junction to Ambient<br>Thermal resistance2|JESD51-9, 2S2P|RJA|39.1|oC/W|
|Junction to Package Top<br>Thermal resistance2|JESD51-9, 2S2P|JT|0.5|oC/W|
|Junction to Case Thermal Resistance3|JESD51-9, 2S2P|RJC|16.2|oC/W|
|Junction to Board Thermal Resistance4|JESD51-8, 2S2P|RJB|23.04|oC/W|



1 Thermal test board meets JEDEC specification for this package (JESD51-9). 

2 Determined in accordance to JEDEC JESD51-2A natural convection environment. Thermal resistance data in this report is solely for a thermal performance comparison of one package to another in a standardized specified environment. It is not meant to predict the performance of a package in an application-specific environment. 

- 3 Junction-to-Case thermal resistance determined using an isothermal cold plate. Case temperature refers to the mold surface temperature at eh package top side dead Centre. 

- 4 Thermal resistance between the die and the printed circuit board per JEDEC JESD51-8. Board temperature is measured on the top surface of the board near the package. 

## **4.1.3 Operating ranges** 

Table 10 provides the operating ranges of the i.MX RT1060 processors. For details on the chip's power structure, see the “Power Management Unit (PMU)” chapter of the _i.MX RT1060 Reference Manual_ (IMXRT1060RM). 

## **Table 10. Operating ranges** 

**==> picture [502 x 245] intentionally omitted <==**

**----- Start of picture text -----**<br>
Parameter  Operating<br>Symbol Min Typ Max [1] Unit Comment<br>Description Conditions<br>Run Mode VDD_SOC_IN Overdrive 1.25 — 1.3 V —<br>VDD_SOC_IN M7 core at 528  1.15 — 1.3 V —<br>MHz<br>M7 core at 132  1.15 — 1.3<br>MHz<br>M7 core at 24  0.925 — 1.3<br>MHz<br>IDLE Mode VDD_SOC_IN M7 core  1.15 — 1.3 V —<br>operation at 528<br>MHz or below<br>SUSPEND (DSM)  VDD_SOC_IN — 0.925 — 1.3 V Refer to Table 13 Low power mode<br>Mode current and power consumption<br>SNVS Mode VDD_SOC_IN — 0 — 1.3 V —<br>Power for DCDC DCDC_IN — 3.0 — 3.6 V —<br>**----- End of picture text -----**<br>


**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

NXP Semiconductors 

25 

## **Electrical Characteristics** 

## **Table 10. Operating ranges (continued)** 

|VDD_HIGH<br>internal Regulator|VDD_HIGH_IN2|—|3.0|—|3.6|V|Must match the range of voltages<br>that the rechargeable backup<br>battery supports.|
|---|---|---|---|---|---|---|---|
|Backup battery<br>supply range|VDD_SNVS_IN3|—|2.40|—|3.6|V|Can be combined with<br>VDD_HIGH_IN, if the system does<br>not require keeping real time and<br>other data on OFF state.|
|USB supply<br>voltages|USB_OTG1_VBUS|—|4.40|—|5.5|V|—|
||USB_OTG2_VBUS|—|4.40|—|5.5|V|—|
|GPIO supplies|NVCC_GPIO|—|3.0|3.3|3.6|V|All digital I/O supplies<br>(NVCC_xxxx) must be powered<br>(unless otherwise specified in this<br>data sheet) under normal<br>conditions whether the associated<br>I/O pins are in use or not.|
||NVCC_SD0|—|1.65|1.8|1.95|V||
||||3.0|3.3|3.6|V||
||NVCC_SD1|—|1.65|1.8|1.95|V||
||||3.0|3.3|3.6|V||
||NVCC_EMC|—|1.65|1.8|1.95|V||
||||3.0|3.3|3.6|V||
|A/D converter|VDDA_ADC_3P3|—|3.0|3.3|3.6|V|VDDA_ADC_3P3 must be<br>powered even if the ADC is not<br>used.<br>VDDA_ADC_3P3 cannot be<br>powered when the other SoC<br>supplies (except VDD_SNVS_IN)<br>are off.|
|System frequency<br>/Bus frequency|FSYS/FBUS|—|24/<br>24|528/<br>132|600/<br>150|MHz|—|
||Temperature Operating Ranges|||||||
|Junction<br>temperature|Tj|Standard<br>Commercial|0|—|95|oC|See the application note, i.MX<br>RT1060 Product Lifetime Usage<br>Estimates for information on<br>product lifetime (power-on years)<br>for this processor.|
|||||||||



1 Applying the maximum voltage results in maximum power consumption and heat generation. NXP recommends a voltage set point = (Vmin + the supply tolerance). This result in an optimized power/speed ratio. 

2 Applying the maximum voltage results in shorten lifetime. 3.6 V usage limited to < 1% of the use profile. Reset of profile limited to below 3.49 V. 

> 3 In setting VDD_SNVS_IN voltage with regards to Charging Currents and RTC, refer to the _i.MX RT1060 Hardware Development Guide_ (IMXRT1060HDG). 

## **4.1.4 External clock sources** 

Each i.MX RT1060 processor has two external input system clocks: a low frequency (RTC_XTALI) and a high frequency (XTALI). 

**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

26 

NXP Semiconductors 

**Electrical Characteristics** 

The RTC_XTALI is used for low-frequency functions. It supplies the clock for wake-up circuit, power-down real time clock operation, and slow system and watch-dog counters. The clock input can be connected to either external oscillator or a crystal using internal oscillator amplifier. Additionally, there is an internal ring oscillator, which can be used instead of the RTC_XTALI if accuracy is not important. 

The system clock input XTALI is used to generate the main system clock. It supplies the PLLs and other peripherals. The system clock input can be connected to either external oscillator or a crystal using internal oscillator amplifier. 

Table 11 shows the interface frequency requirements. 

**Table 11. External input clock frequency** 

|**Parameter Description**|**Symbol**|**Min**|**Typ**|**Max**|**Unit**|
|---|---|---|---|---|---|
|RTC_XTALI Oscillator1,2|fckil|—|32.7683/32.0|—|kHz|
|XTALI Oscillator2,4|fxtal|—|24|—|MHz|



1 External oscillator or a crystal with internal oscillator amplifier. 

- 2 The required frequency stability of this clock source is application dependent. For recommendations, see the Hardware Development Guide for _i.MX RT1060 Crossover Processors_ (IMXRT1060HDG). 

- 3 Recommended nominal frequency 32.768 kHz. 

4 External oscillator or a fundamental frequency crystal with internal oscillator amplifier. 

The typical values shown in Table 11 are required for use with NXP SDK to ensure precise time keeping and USB operation. For RTC_XTALI operation, two clock sources are available. 

- On-chip 40 kHz ring oscillator—this clock source has the following characteristics: 

   - Approximately 25 µA more Idd than crystal oscillator 

   - Approximately ±50% tolerance 

   - No external component required 

   - Starts up quicker than 32 kHz crystal oscillator 

- External crystal oscillator with on-chip support circuit: 

   - At power up, ring oscillator is utilized. After crystal oscillator is stable, the clock circuit switches over to the crystal oscillator automatically. 

   - Higher accuracy than ring oscillator 

   - If no external crystal is present, then the ring oscillator is utilized 

The decision of choosing a clock source should be taken based on real-time clock use and precision time-out. 

## **4.1.5 Maximum supply currents** 

The data shown in Table 12 represent a use case designed specifically to show the maximum current consumption possible. All cores are running at the defined maximum frequency and are limited to L1 cache accesses only to ensure no pipeline stalls. Although a valid condition, it would have a very limited practical use case, if at all, and be limited to an extremely low duty cycle unless the intention were to specifically show the worst case power consumption. 

**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

NXP Semiconductors 

27 

## **Electrical Characteristics** 

See the _i.MX RT1060 Power Consumption Measurement Application Note_ for more details on typical power consumption under various use case definitions. 

**Table 12. Maximum supply currents** 

|**Power Rail**|**Conditions**|**Max Current**|**Unit**|
|---|---|---|---|
|DCDC_IN|Max power for chip at 95oC with core<br>mark run on FlexRAM|110|mA|
|VDD_HIGH_IN|Include internal loading in analog|50|mA|
|VDD_SNVS_IN|—|250|A|
|USB_OTG1_VBUS<br>USB_OTG2_VBUS|25 mA for each active USB interface|50|mA|
|VDDA_ADC_3P3|3.3 V power supply for 12-bit ADC, 600<br>A typical, 750A max, for each ADC.<br>100 Ohm max loading for touch panel,<br>cause 33 mA current.|40|mA|
|NVCC_GPIO<br>NVCC_SD0<br>NVCC_SD1<br>NVCC_EMC|Imax = N x C x V x (0.5 x F)<br>Where:<br>N—Number of IO pins supplied by the power line<br>C—Equivalent external capacitive load<br>V—IO voltage<br>(0.5 x F)—Data change rate. Up to 0.5 of the clock rate (F)<br>In this equation, Imax is in Amps, C in Farads, V in Volts, and F in Hertz.|||



**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

28 

NXP Semiconductors 

**Electrical Characteristics** 

## **4.1.6 Low power mode supply currents** 

Table 13 shows the current core consumption (not including I/O) of i.MX RT1060 processors in selected low power modes. 

**Table 13. Low power mode current and power consumption** 

|**Mode**|**Test Conditions**|**Supply**|**Typical1**|**Units**|
|---|---|---|---|---|
|SYSTEM IDLE|• LDO_2P5 set to 2.5 V, LDO_1P1 set to 1.1 V<br>• CPU in WFI, CPU clock gated<br>• 24 MHz XTAL is ON<br>• System PLL is active, other PLLs are power down<br>• Peripheral clock gated, but remain powered<br>• 1024 KB RAM retention|DCDC_IN (3.3 V)|4.04|mA|
|||VDD_HIGH_IN (3.3 V)|7.66||
|||VDD_SNVS_IN (3.3 V)|0.032||
|||Total|38.72|mW|
|LOW POWER IDLE|• LDO_2P5 and LDO_1P1 are set to Weak mode<br>• WFI, half FlexRAM power down in power gate<br>mode<br>• All PLLs are power down<br>• 24 MHz XTAL is off, 24 MHz RCOSC used as<br>clock source<br>• Peripheral clock gated, but remain powered<br>• 1024 KB RAM retention|DCDC_IN (3.3 V)|1.11|mA|
|||VDD_HIGH_IN (3.3 V)|0.309||
|||VDD_SNVS_IN (3.3 V)|0.048||
|||Total|4.84|mW|
|SUSPEND<br>(DSM)|• LDO_2P5 and LDO_1P1 are shut off<br>• CPU in Power Gate mode<br>• All PLLs are power down<br>• 24 MHz XTAL is off, 24 MHz RCOSC is off<br>• All clocks are shut off, except 32 kHz RTC<br>• Peripheral clock gated, but remain powered<br>• 64 KB RAM retention|DCDC_IN (3.3 V)|0.19|mA|
|||VDD_HIGH_IN (3.3 V)|0.029||
|||VDD_SNVS_IN (3.3 V)|0.020||
|||Total|0.789|mW|
|SNVS (RTC)|• All SOC digital logic, analog module are shut off<br>• 32 kHz RTC is alive|DCDC_IN (0 V)|0|mA|
|||VDD_HIGH_IN (0 V)|0||
|||VDD_SNVS_IN (3.3 V)|0.02||
|||Total|0.066|mW|
||||||



1 The typical values shown here are for information only and are not guaranteed. These values are average values measured on a typical process wafer at 25[o] C. 

## **4.1.7 USB PHY current consumption** 

## **4.1.7.1 Power down mode** 

In power down mode, everything is powered down, including the USB VBUS valid detectors in typical condition. Table 14 shows the USB interface current consumption in power down mode. 

**Table 14. USB PHY current consumption in power down mode** 

||**VDD_USB_CAP (3.0 V)**|**VDD_HIGH_CAP (2.5 V)**|**NVCC_PLL (1.1 V)**|
|---|---|---|---|
|Current|5.1A|1.7A|< 0.5A|



**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

NXP Semiconductors 

29 

**Electrical Characteristics** 

## **NOTE** 

The currents on the VDD_HIGH_CAP and VDD_USB_CAP were identified to be the voltage divider circuits in the USB-specific level shifters. 

## **4.2 System power and clocks** 

This section provide the information about the system power and clocks. 

## **4.2.1 Power supplies requirements and restrictions** 

The system design must comply with power-up sequence, power-down sequence, and steady state guidelines as described in this section to guarantee the reliable operation of the device. Any deviation from these sequences may result in the following situations: 

- Excessive current during power-up phase 

- Prevention of the device from booting 

- Irreversible damage to the processor (worst-case scenario) 

## **4.2.1.1 Power-up sequence** 

The below restrictions must be followed: 

- VDD_SNVS_IN supply must be turned on before any other power supply or be connected (shorted) with VDD_HIGH_IN supply. 

- If a coin cell is used to power VDD_SNVS_IN, then ensure that it is connected before any other supply is switched on. 

- An RC delay circuit is recommended for providing the delay between DCDC_IN stable and DCDC_PSWITCH. The total RC delay should be 5-15 ms. 

- DCDC_IN must reach a minimum 3.0 V within 0.3 x RC. 

- Delay from DCDC_IN stable at 3.0 V min to DCDC_PSWITCH reaching 0.5 x DCDC_IN (1.5 V) must be at least 1 ms. 

- Power up slew rate specification for other power domains is 360V/s – 36kV/s. 

## **NOTE** 

To release MCU by POR_B signal, the POR_B input must be immediately asserted at power-up and remain asserted until the last power rail reaches its working voltage. In the absence of an external reset feeding the POR_B input, the internal POR module takes control. See the _i.MX RT1060 Reference Manual_ (IMXRT1060RM) for further details and to ensure that all necessary requirements are being met. 

## **NOTE** 

Need to ensure that there is no back voltage (leakage) from any supply on the board towards the 3.3 V supply (for example, from the external components that use both the 1.8 V and 3.3 V supplies). 

**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

30 

NXP Semiconductors 

**Electrical Characteristics** 

## **NOTE** 

USB_OTG1_VBUS and USB_OTG2_VBUS are not part of the power supply sequence and may be powered at any time. 

## **4.2.1.2 Power-down sequence** 

The following restrictions must be followed: 

- VDD_SNVS_IN supply must be turned off after any other power supply or be connected (shorted) with VDD_HIGH_IN supply. 

- If a coin cell is used to power VDD_SNVS_IN, then ensure that it is removed after any other supply is switched off. 

## **4.2.1.3 Power supplies usage** 

All I/O pins should not be externally driven while the I/O power supply for the pin (NVCC_xxx) is OFF. This can cause internal latch-up and malfunctions due to reverse current flows. For information about I/O power supply of each pin, see “Power Rail” columns in pin list tables of Section 6, Package information and contact assignments.” 

## **4.2.2 Integrated LDO voltage regulator parameters** 

Various internal supplies can be powered ON from internal LDO voltage regulators. All the supply pins named *_CAP must be connected to external capacitors. The on-board LDOs are intended for internal use only and should not be used to power any external circuitry. See the _i.MX RT1060 Reference Manual_ (IMXRT1060RM) for details on the power tree scheme. 

## **NOTE** 

The *_CAP signals should not be powered externally. These signals are intended for internal LDO operation only. 

## **4.2.2.1 Digital regulators (LDO_SNVS)** 

There are one digital LDO regulator (“Digital”, because of the logic loads that they drive, not because of their construction). The advantages of the regulator is to reduce the input supply variation because of its input supply ripple rejection and its on-die trimming. This translates into more stable voltage for the on-chip logics. 

The regulator has two basic modes: 

- Power Gate. The regulation FET is switched fully off limiting the current draw from the supply. The analog part of the regulator is powered down here limiting the power consumption. 

- Analog regulation mode. The regulation FET is controlled such that the output voltage of the regulator equals the target voltage. 

For additional information, see the _i.MX RT1060 Reference Manual_ (IMXRT1060RM). 

**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

NXP Semiconductors 

31 

**Electrical Characteristics** 

## **4.2.2.2 Regulators for analog modules** 

## **4.2.2.2.1 LDO_1P1** 

The LDO_1P1 regulator implements a programmable linear-regulator function from VDD_HIGH_IN (see Table 10 for minimum and maximum input requirements). Typical Programming Operating Range is 1.0 V to 1.2 V with the nominal default setting as 1.1 V. The LDO_1P1 supplies the USB Phy, and PLLs. A programmable brown-out detector is included in the regulator that can be used by the system to determine when the load capability of the regulator is being exceeded to take the necessary steps. Current-limiting can be enabled to allow for in-rush current requirements during start-up, if needed. Active-pull-down can also be enabled for systems requiring this feature. 

For information on external capacitor requirements for this regulator, see the _Hardware Development Guide for i.MX RT1060 Crossover Processors_ (IMXRT1060HDG). 

For additional information, see the _i.MX RT1060 Reference Manual_ (IMXRT1060RM). 

## **4.2.2.2.2 LDO_2P5** 

The LDO_2P5 module implements a programmable linear-regulator function from VDD_HIGH_IN (see Table 10 for minimum and maximum input requirements). Typical Programming Operating Range is 2.25 V to 2.75 V with the nominal default setting as 2.5 V. LDO_2P5 supplies the USB PHY, E-fuse module, and PLLs. A programmable brown-out detector is included in the regulator that can be used by the system to determine when the load capability of the regulator is being exceeded, to take the necessary steps. Current-limiting can be enabled to allow for in-rush current requirements during start-up, if needed. Active-pull-down can also be enabled for systems requiring this feature. An alternate self-biased low-precision weak-regulator is included that can be enabled for applications needing to keep the output voltage alive during low-power modes where the main regulator driver and its associated global bandgap reference module are disabled. The output of the weak-regulator is not programmable and is a function of the input supply as well as the load current. Typically, with a 3 V input supply the weak-regulator output is 2.525 V and its output impedance is approximately 40 . 

For information on external capacitor requirements for this regulator, see the _Hardware Development Guide for i.MX RT1060 Crossover Processors_ (IMXRT1060HDG). 

For additional information, see the _i.MX RT1060 Reference Manual_ (IMXRT1060RM). 

## **4.2.2.2.3 LDO_USB** 

The LDO_USB module implements a programmable linear-regulator function from the USB VUSB voltages (4.4 V–5.5 V) to produce a nominal 3.0 V output voltage. A programmable brown-out detector is included in the regulator that can be used by the system to determine when the load capability of the regulator is being exceeded, to take the necessary steps. This regulator has a built in power-mux that allows the user to select to run the regulator from either USB VBUS supply, when both are present. If only one of the USB VBUS voltages is present, then, the regulator automatically selects this supply. Current limit is also included to help the system meet in-rush current targets. 

For information on external capacitor requirements for this regulator, see the _Hardware Development Guide for i.MX RT1060 Crossover Processors_ (IMXRT1060HDG). 

**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

32 

NXP Semiconductors 

**Electrical Characteristics** 

For additional information, see the _i.MX RT1060 Reference Manual_ (IMXRT1060RM). 

## **4.2.2.2.4 DCDC** 

DCDC can be configured to operate on power-save mode when the load current is less than 50 mA. During the power-save mode, the converter operates with reduced switching frequency in PFM mode and with a minimum quiescent current to maintain high efficiency. 

DCDC can detect the peak current in the P-channel switch. When the peak current exceeds the threshold, DCDC will give an alert signal, and the threshold can be configured. By this way, DCDC can roughly detect the current loading. 

DCDC also includes the following protection functions: 

- Over current protection. In run mode, DCDC shuts down when detecting abnormal large current in the P-type power switch. 

- Over voltage protection. DCDC shuts down when detecting the output voltage is too high. 

- Low voltage detection. DCDC shuts down when detecting the input voltage is too low. 

For additional information, see the _i.MX RT1060 Reference Manual_ (IMXRT1060RM). 

## **4.2.3 PLL’s electrical characteristics** 

This section provides PLL electrical characteristics. 

## **4.2.3.1 Audio/Video PLL’s electrical parameters** 

**Table 15. Audio/Video PLL’s electrical parameters** 

|**Parameter**|**Value**|
|---|---|
|Clock output range|650 MHz ~1.3 GHz|
|Reference clock|24 MHz|
|Lock time|< 11250 reference cycles|



## **4.2.3.2 System PLL** 

**Table 16. System PLL’s electrical parameters** 

|**Parameter**|**Value**|
|---|---|
|Clock output range|528 MHz PLL output|
|Reference clock|24 MHz|
|Lock time|< 11250 reference cycles|



**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

NXP Semiconductors 

33 

## **Electrical Characteristics** 

## **4.2.3.3 Ethernet PLL** 

## **Table 17. Ethernet PLL’s electrical parameters** 

|**Parameter**|**Value**|
|---|---|
|Clock output range|1 GHz|
|Reference clock|24 MHz|
|Lock time|< 11250 reference cycles|



## **4.2.3.4 USB PLL** 

**Table 18. USB PLL’s electrical parameters** 

|**Parameter**|**Value**|
|---|---|
|Clock output range|480 MHz PLL output|
|Reference clock|24 MHz|
|Lock time|< 383 reference cycles|



## **4.2.3.5 Arm PLL** 

## **Table 19. Arm PLL’s electrical parameters** 

|**Parameter**|**Value**|
|---|---|
|Clock output range|648 MHz ~ 1296 MHz|
|Reference clock|24 MHz|
|Lock time|< 2250 reference cycles|



## **4.2.4 On-chip oscillators** 

## **4.2.4.1 OSC24M** 

This block implements an amplifier that when combined with a suitable quartz crystal and external load capacitors implement an oscillator. The oscillator is powered from NVCC_PLL. 

The system crystal oscillator consists of a Pierce-type structure running off the digital supply. A straight forward biased-inverter implementation is used. 

## **4.2.4.2 OSC32K** 

This block implements an amplifier that when combined with a suitable quartz crystal and external load capacitors implement a low power oscillator. It also implements a power mux such that it can be powered from either a ~3 V backup battery (VDD_SNVS_IN) or VDD_HIGH_IN such as the oscillator consumes 

**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

34 

NXP Semiconductors 

**Electrical Characteristics** 

power from VDD_HIGH_IN when that supply is available and transitions to the backup battery when VDD_HIGH_IN is lost. 

In addition, if the clock monitor determines that the OSC32K is not present, then the source of the 32 K will automatically switch to a crude internal ring oscillator. The frequency range of this block is approximately 10–45 kHz. It highly depends on the process, voltage, and temperature. 

The OSC32k runs from VDD_SNVS_CAP supply, which comes from the VDD_HIGH_IN/VDD_SNVS_IN. The target battery is a ~3 V coin cell. Proper choice of coin cell type is necessary for chosen VDD_HIGH_IN range. Appropriate series resistor (Rs) must be used when connecting the coin cell. Rs depends on the charge current limit that depends on the chosen coin cell. For example, for Panasonic ML621: 

- Average Discharge Voltage is 2.5 V 

- Maximum Charge Current is 0.6 mA 

For a charge voltage of 3.2 V, Rs = (3.2-2.5)/0.6 m = 1.17 k. 

## **Table 20. OSC32K main characteristics** 

||**Min**|**Typ**|**Max**|**Comments**|
|---|---|---|---|---|
|Fosc|—|32.768 kHz|—|This frequency is nominal and determined mainly by the crystal selected.<br>32.0 K would work as well.|
|Current consumption|—|4A|—|The 4A is the consumption of the oscillator alone (OSC32k). Total supply<br>consumption will depend on what the digital portion of the RTC consumes.<br>The ring oscillator consumes 1A when ring oscillator is inactive, 20A<br>when the ring oscillator is running. Another 1.5A is drawn from vdd_rtc in<br>the power_detect block. So, the total current is 6.5A on vdd_rtc when the<br>ring oscillator is not running.|
|Bias resistor|—|14 M|—|This integrated bias resistor sets the amplifier into a high gain state. Any<br>leakage through the ESD network, external board leakage, or even a<br>scope probe that is significant relative to this value will debias the amp. The<br>debiasing will result in low gain, and will impact the circuit's ability to start<br>up and maintain oscillations.|
|**Crystal Properties**|||||
|Cload|—|10 pF|—|Usually crystals can be purchased tuned for different Cloads. This Cload<br>value is typically 1/2 of the capacitances realized on the PCB on either side<br>of the quartz. A higher Cload will decrease oscillation margin, but<br>increases current oscillating through the crystal.|
|ESR|—|50 k|100 k|Equivalent series resistance of the crystal. Choosing a crystal with a higher<br>value will decrease the oscillating margin.|



## **4.3 I/O parameters** 

This section provide parameters on I/O interfaces. 

## **4.3.1 I/O DC parameters** 

This section includes the DC parameters of the following I/O types: 

**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

NXP Semiconductors 

35 

**Electrical Characteristics** 

- XTALI and RTC_XTALI (Clock Inputs) DC Parameters 

- General Purpose I/O (GPIO) 

- LVDS I/O DC Parameters 

## **NOTE** 

The term ‘NVCC_XXXX’ in this section refers to the associated supply rail of an input or output. 

**==> picture [377 x 138] intentionally omitted <==**

**Figure 3. Circuit for parameters Voh and Vol for I/O cells** 

## **4.3.1.1 XTALI and RTC_XTALI (clock inputs) DC parameters** 

Table 21 shows the DC parameters for the clock inputs. 

## **Table 21. XTALI and RTC_XTALI DC parameters[1]** 

|**Parameter**|**Symbol**|**Test Conditions**|**Min**|**Max**|**Unit**|
|---|---|---|---|---|---|
|XTALI high-level DC input voltage|Vih|—|0.8 x NVCC_PLL|NVCC_PLL|V|
|XTALI low-level DC input voltage|Vil|—|0|0.2|V|
|RTC_XTALI high-level DC input voltage|Vih|—|0.8|1.1|V|
|RTC_XTALI low-level DC input voltage|Vil|—|0|0.2|V|



1 The DC parameters are for external clock input only. 

## **4.3.1.2 Single voltage general purpose I/O (GPIO) DC parameters** 

Table 22 shows DC parameters for GPIO pads. The parameters in Table 22 are guaranteed per the operating ranges in Table 10, unless otherwise noted. 

**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

36 

NXP Semiconductors 

**Electrical Characteristics** 

**Table 22. Single voltage GPIO DC parameters** 

|**Parameter**|**Symbol**|**Test Conditions**|**Min**|**Typical**|**Max**|**Units**|
|---|---|---|---|---|---|---|
|High-level output voltage1|VOH|Ioh= -0.1mA (ipp_dse=001,010)<br>Ioh= -1mA<br>(ipp_dse=011,100,101,110,111)|NVCC_XXX<br>X-0.15|—|–|V|
|Low-level output voltage1|VOL|Iol= 0.1mA (ipp_dse=001,010)<br>Iol= 1mA<br>(ipp_dse=011,100,101,110,111)|–|—|0.15|V|
|High-level output current|IOH|VDDE= 3.3 V, VOH= VDDE- 0.45<br>V, ipp_dse as follows:<br>001<br>010<br>011<br>110<br>101<br>110<br>111|—|-1<br>-1<br>-2<br>-2<br>-2<br>-4<br>-4|—|mA|
|Low-level output current|IOL|VDDE= 3.3 V, VOL= 0.45 V,<br>ipp_dse as follows:<br>001<br>010<br>011<br>110<br>101<br>110<br>111|—|1<br>1<br>2<br>2<br>2<br>4<br>4|—|mA|
|High-Level input voltage1,2|VIH|—|0.7 x<br>NVCC_XXX<br>X|—|NVCC_XX<br>XX|V|
|Low-Level input voltage1,2|VIL|—|0|—|0.3 x<br>NVCC_XX<br>XX|V|
|Input Hysteresis<br>(NVCC_XXXX= 1.8V)|VHYS_LowV<br>DD|NVCC_XXXX=1.8V|250|—|—|mV|
|Input Hysteresis<br>(NVCC_XXXX=3.3V)|VHYS_HighV<br>DD|NVCC_XXXX=3.3V|250|—|—|mV|
|Schmitt trigger VT+2,3|VTH+|—|0.5 x<br>NVCC_XXX<br>X|—|—|mV|
|Schmitt trigger VT-2,3|VTH-|—|—|—|0.5 x<br>NVCC_XX<br>XX|mV|
|Pull-up resistor (22_kPU)|RPU_22K|Vin=0V|—|—|212|A|
|Pull-up resistor (22_kPU)|RPU_22K|Vin=NVCC_XXXX|—|—|1|A|
|Pull-up resistor (47_kPU)|RPU_47K|Vin=0V|—|—|100|A|
|Pull-up resistor (47_kPU)|RPU_47K|Vin=NVCC_XXXX|—|—|1|A|



**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

NXP Semiconductors 

37 

## **Electrical Characteristics** 

**Table 22. Single voltage GPIO DC parameters (continued)** 

||||||||
|---|---|---|---|---|---|---|
|**Parameter**|**Symbol**|**Test Conditions**|**Min**|**Typical**|**Max**|**Units**|
|Pull-up resistor (100_k<br>PU)|RPU_100K|Vin=0V|—|—|48|A|
|Pull-up resistor (100_k<br>PU)|RPU_100K|Vin=NVCC_XXXX|—|—|1|A|
|Pull-down resistor (100_k<br>PD)|RPD_100K|Vin=NVCC_XXXX|—|—|48|A|
|Pull-down resistor (100_k<br>PD)|RPD_100K|Vin=0V|—|—|1|A|
|Input current (no PU/PD)|IIN|VI = 0, VI = NVCC_XXXX|-1|—|1|A|
|Keeper Circuit Resistance|R_Keeper|VI =0.3 x NVCC_XXXX, VI = 0.7<br>x NVCC_XXXX|105|—|175|k|
||||||||



1 Overshoot and undershoot conditions (transitions above NVCC_XXXX and below GND) on switching pads must be held below 0.6 V, and the duration of the overshoot/undershoot must not exceed 10% of the system clock cycle. Overshoot/ undershoot must be controlled through printed circuit board layout, transmission line impedance matching, signal line termination, or other methods. Non-compliance to this specification may affect device reliability or cause permanent damage to the device. 

2 To maintain a valid level, the transition edge of the input must sustain a constant slew rate (monotonic) from the current DC level through to the target DC level, Vil or Vih. Monotonic input transition time is from 0.1 ns to 1 s. 

3 Hysteresis of 250 mV is guaranteed over all operating conditions when hysteresis is enabled. 

## **4.3.1.3 LVDS I/O DC parameters** 

The LVDS interface complies with TIA/EIA 644-A standard. See TIA/EIA STANDARD 644-A, “Electrical Characteristics of Low Voltage Differential Signaling (LVDS) Interface Circuits” for details. 

Table 23 shows the Low Voltage Differential Signaling (LVDS) I/O DC parameters. 

## **Table 23. LVDS I/O DC characteristics[1]** 

|**Parameter**|**Symbol**|**Test Conditions**|**Min**|**Typ**|**Max**|**Unit**|
|---|---|---|---|---|---|---|
|Output Differential Voltage|VOD|Rload-100Diff|250|350|450|mV|
|Output High Voltage|VOH|IOH = 0 mA|1.25|1.375|1.6|V|
|Output Low Voltage|VOL|IOL = 0 mA|0.9|1.025|1.25|V|
|Offset Voltage|VOS|—|1.125|1.2|1.375|V|



1 Note: The LVDS interface is limited to CCM_CLK1_P and CCM_CLK1_N. 

## **4.3.2 I/O AC parameters** 

This section includes the AC parameters of the following I/O types: 

- General Purpose I/O (GPIO) 

Figure 4 shows load circuit for output, and Figure 5 show the output transition time waveform. 

**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

38 

NXP Semiconductors 

**Electrical Characteristics** 

**==> picture [207 x 60] intentionally omitted <==**

**----- Start of picture text -----**<br>
From Output Test Point<br>Under Test<br>CL<br>CL includes package, probe and fixture capacitance<br>**----- End of picture text -----**<br>


**Figure 4. Load circuit for output** 

**==> picture [381 x 62] intentionally omitted <==**

**----- Start of picture text -----**<br>
OVDD<br>80% 80%<br>20% 20%<br>Output (at pad) 0 V<br>tr tf<br>**----- End of picture text -----**<br>


**Figure 5. Output transition time waveform** 

## **4.3.2.1 General purpose I/O AC parameters** 

The I/O AC parameters for GPIO in slow and fast modes are presented in the Table 24 and Table 25, respectively. Note that the fast or slow I/O behavior is determined by the appropriate control bits in the IOMUXC control registers. 

**Table 24. General purpose I/O AC parameters 1.8 V mode** 

|**Parameter**|**Symbol**|**Test Condition**|**Min**|**Typ**|**Max**|**Unit**|
|---|---|---|---|---|---|---|
|Output Pad Transition Times, rise/fall<br>(Max Drive, ipp_dse=111)|tr, tf|15 pF Cload, slow slew rate<br>15 pF Cload, fast slew rate|—|—|2.72/2.79<br>1.51/1.54|ns|
|Output Pad Transition Times, rise/fall<br>(High Drive, ipp_dse=101)|tr, tf|15 pF Cload, slow slew rate<br>15 pF Cload, fast slew rate|—|—|3.20/3.36<br>1.96/2.07||
|Output Pad Transition Times, rise/fall<br>(Medium Drive, ipp_dse=100)|tr, tf|15 pF Cload, slow slew rate<br>15 pF Cload, fast slew rate|—|—|3.64/3.88<br>2.27/2.53||
|Output Pad Transition Times, rise/fall<br>(Low Drive. ipp_dse=011)|tr, tf|15 pF Cload, slow slew rate<br>15 pF Cload, fast slew rate|—|—|4.32/4.50<br>3.16/3.17||
|Input Transition Times1|trm|—|—|—|25|ns|



1 Hysteresis mode is recommended for inputs with transition times greater than 25 ns. 

**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

NXP Semiconductors 

39 

## **Electrical Characteristics** 

**Table 25. General purpose I/O AC parameters 3.3 V mode** 

|**Parameter**|**Symbol**|**Test Condition**|**Min**|**Typ**|**Max**|**Unit**|
|---|---|---|---|---|---|---|
|Output Pad Transition Times, rise/fall<br>(Max Drive, ipp_dse=101)|tr, tf|15 pF Cload, slow slew rate<br>15 pF Cload, fast slew rate|—|—|1.70/1.79<br>1.06/1.15|ns<br>ns|
|Output Pad Transition Times, rise/fall<br>(High Drive, ipp_dse=011)|tr, tf|15 pF Cload, slow slew rate<br>15 pF Cload, fast slew rate|—|—|2.35/2.43<br>1.74/1.77||
|Output Pad Transition Times, rise/fall<br>(Medium Drive, ipp_dse=010)|tr, tf|15 pF Cload, slow slew rate<br>15 pF Cload, fast slew rate|—|—|3.13/3.29<br>2.46/2.60||
|Output Pad Transition Times, rise/fall<br>(Low Drive. ipp_dse=001)|tr, tf|15 pF Cload, slow slew rate<br>15 pF Cload, fast slew rate|—|—|5.14/5.57<br>4.77/5.15||
|Input Transition Times1|trm|—|—|—|25|ns|



1 Hysteresis mode is recommended for inputs with transition times greater than 25 ns. 

## **4.3.3 Output buffer impedance parameters** 

This section defines the I/O impedance parameters of the i.MX RT1060 processors for the following I/O types: 

- Single Voltage General Purpose I/O (GPIO) 

## **NOTE** 

GPIO I/O output driver impedance is measured with “long” transmission line of impedance Ztl attached to I/O pad and incident wave launched into transmission line. Rpu/Rpd and Ztl form a voltage divider that defines specific voltage of incident wave relative to NVCC_XXXX. Output driver impedance is calculated from this voltage divider (see Figure 6). 

**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

40 

NXP Semiconductors 

**Electrical Characteristics** 

**==> picture [436 x 430] intentionally omitted <==**

**----- Start of picture text -----**<br>
OVDD<br>PMOS (Rpu)<br>Ztl , L = 20 inches<br>ipp_do pad<br>predriver<br>Cload = 1p<br>NMOS (Rpd)<br>OVSS<br>U,(V)<br>Vin (do)<br>VDD<br>t,(ns)<br>0<br>U,(V)<br>Vout (pad)<br>OVDD<br>Vref2<br>Vref1<br>Vref<br>t,(ns)<br>0<br>Vovdd - Vref1 Vref2<br>Rpu =   Ztl Rpd =   Ztl<br>Vref1 Vovdd - Vref2<br>**----- End of picture text -----**<br>


**Figure 6. Impedance matching load for measurement** 

**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

NXP Semiconductors 

41 

**Electrical Characteristics** 

## **4.3.3.1 Single voltage GPIO output buffer impedance** 

Table 26 shows the GPIO output buffer impedance (NVCC_XXXX 1.8 V). 

**Table 26. GPIO output buffer average impedance (NVCC_XXXX 1.8 V)** 

|**Parameter**|**Symbol**|**Drive Strength (DSE)**|**Typ Value**|**Unit**|
|---|---|---|---|---|
|Output Driver<br>Impedance|Rdrv|001<br>010<br>011<br>100<br>101<br>110<br>111|260<br>130<br>88<br>65<br>52<br>43<br>37||



Table 27 shows the GPIO output buffer impedance (NVCC_XXXX 3.3 V). 

**Table 27. GPIO output buffer average impedance (NVCC_XXXX 3.3 V)** 

|**Parameter**|**Symbol**|**Drive Strength (DSE)**|**Typ Value**|**Unit**|
|---|---|---|---|---|
|Output Driver<br>Impedance|Rdrv|001<br>010<br>011<br>100<br>101<br>110<br>111|157<br>78<br>53<br>39<br>32<br>26<br>23||



## **4.4 System modules** 

This section contains the timing and electrical parameters for the modules in the i.MX RT1060 processor. 

## **4.4.1 Reset timings parameters** 

Figure 7 shows the reset timing and Table 28 lists the timing parameters. 

**==> picture [194 x 67] intentionally omitted <==**

**----- Start of picture text -----**<br>
POR_B<br>(Input)<br>CC1<br>Figure 7. Reset timing diagram<br>**----- End of picture text -----**<br>


## **Table 28. Reset timing parameters** 

**==> picture [506 x 42] intentionally omitted <==**

**----- Start of picture text -----**<br>
ID Parameter Min Max Unit<br>CC1 Duration of POR_B to be qualified as valid. 1 — RTC_XTALI cycle<br>**----- End of picture text -----**<br>


**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

42 

NXP Semiconductors 

**Electrical Characteristics** 

## **4.4.2 WDOG reset timing parameters** 

Figure 8 shows the WDOG reset timing and Table 29 lists the timing parameters. 

||||WDOGn_B|||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|
||||(Output)|||CC3||||||
|||||**Figure 8. WDOGn_B**||**timing**|**diagram**|||||
|||||**Table 29. WDOGn_B timing parameters**||||||||
|**ID**||||**Parameter**|||||**Min**|**Max**|**Unit**|
|CC3|Duration|of|WDOGn_B|Assertion|||||1|—|RTC_XTALI cycle|



## **NOTE** 

RTC_XTALI is approximately 32 kHz. RTC_XTALI cycle is one period or approximately 30 s. 

## **NOTE** 

WDOGn_B output signals (for each one of the Watchdog modules) do not have dedicated pins, but are muxed out through the IOMUX. See the IOMUX manual for detailed information. 

## **4.4.3 SCAN JTAG Controller (SJC) timing parameters** 

Figure 9 depicts the SJC test clock input timing. Figure 10 depicts the SJC boundary scan timing. Figure 11 depicts the SJC test access port. Signal parameters are listed in Table 30. 

**==> picture [403 x 101] intentionally omitted <==**

**----- Start of picture text -----**<br>
SJ1<br>SJ2 SJ2<br>JTAG_TCK<br>(Input) VIH VM VM<br>VIL<br>SJ3 SJ3<br>Figure 9. Test clock input timing diagram<br>**----- End of picture text -----**<br>


**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

NXP Semiconductors 

43 

**Electrical Characteristics** 

**==> picture [407 x 237] intentionally omitted <==**

**----- Start of picture text -----**<br>
JTAG_TCK<br>(Input) VIH<br>VIL<br>SJ4 SJ5<br>Data<br>Input Data Valid<br>Inputs<br>SJ6<br>Data<br>Output Data Valid<br>Outputs<br>SJ7<br>Data<br>Outputs<br>SJ6<br>Data<br>Output Data Valid<br>Outputs<br>**----- End of picture text -----**<br>


**Figure 10. Boundary Scan (JTAG) timing diagram** 

**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

44 

NXP Semiconductors 

**Electrical Characteristics** 

**==> picture [502 x 633] intentionally omitted <==**

**----- Start of picture text -----**<br>
JTAG_TCK<br>(Input) VIH<br>VIL<br>SJ8 SJ9<br>JTAG_TDI<br>JTAG_TMS Input Data Valid<br>(Input)<br>SJ10<br>JTAG_TDO<br>Output Data Valid<br>(Output)<br>SJ11<br>JTAG_TDO<br>(Output)<br>SJ10<br>JTAG_TDO<br>Output Data Valid<br>(Output)<br>Figure 11. Test access port timing diagram<br>JTAG_TCK<br>(Input)<br>SJ13<br>JTAG_TRST_B<br>(Input)<br>SJ12<br>Figure 12. JTAG_TRST_B timing diagram<br>Table 30. JTAG timing<br>All Frequencies<br>ID Parameter [1,2] Unit<br>Min Max<br>SJ0 JTAG_TCK frequency of operation 1/(3•TDC) [1] 0.001 22 MHz<br>SJ1 JTAG_TCK cycle time in crystal mode 45 — ns<br>SJ2 JTAG_TCK clock pulse width measured at VM [2] 22.5 — ns<br>SJ3 JTAG_TCK rise and fall times — 3 ns<br>SJ4 Boundary scan input data set-up time 5 — ns<br>SJ5 Boundary scan input data hold time 24 — ns<br>SJ6 JTAG_TCK low to output data valid  — 40 ns<br>SJ7 JTAG_TCK low to output high impedance — 40 ns<br>SJ8 JTAG_TMS, JTAG_TDI data set-up time 5 — ns<br>**----- End of picture text -----**<br>


**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

NXP Semiconductors 

45 

**Electrical Characteristics** 

## **Table 30. JTAG timing (continued)** 

|**ID**|**Parameter1,2**|**All Frequencies**|**All Frequencies**|**Unit**|
|---|---|---|---|---|
|||**Min**|**Max**||
|SJ9|JTAG_TMS, JTAG_TDI data hold time|25|—|ns|
|SJ10|JTAG_TCK low to JTAG_TDO data valid|—|44|ns|
|SJ11|JTAG_TCK low to JTAG_TDO high impedance|—|44|ns|
|SJ12|JTAG_TRST_B assert time|100|—|ns|
|SJ13|JTAG_TRST_B set-up time to JTAG_TCK low|40|—|ns|



1 TDC = target frequency of SJC 

> 2 VM = mid-point voltage 

## **4.4.4 Debug trace timing specifications** 

## **Table 31. Debug trace operating behaviors** 

|**Symbol**|**Description**|**Min**|**Max**|**Unit**|
|---|---|---|---|---|
|T1|ARM_TRACE_CLK frequency of operation|—|70|MHz|
|T2|ARM_TRACE_CLK period|1/T1|—|MHz|
|T3|Low pulse width|6|—|ns|
|T4|High pulse width|6|—|ns|
|T5|Clock and data rise time|—|1|ns|
|T6|Clock and data fall time|—|1|ns|
|T7|Data setup|2|—|ns|
|T8|Data hold|0.7|—|ns|



**==> picture [487 x 96] intentionally omitted <==**

**----- Start of picture text -----**<br>
�������������<br>�� T6<br>T4 ��<br>��<br>**----- End of picture text -----**<br>


**Figure 13. ARM_TRACE_CLK specifications** 

**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

46 

NXP Semiconductors 

**Electrical Characteristics** 

**==> picture [395 x 57] intentionally omitted <==**

**----- Start of picture text -----**<br>
ARM_TRACE_CLK<br>T7 T8 T7 T8<br>ARM_TRACE0-3<br>**----- End of picture text -----**<br>


**==> picture [35 x 33] intentionally omitted <==**

**Figure 14. Trace data specifications** 

## **4.5 External memory interface** 

The following sections provide information about external memory interfaces. 

## **4.5.1 SEMC specifications** 

The following sections provide information on SEMC interface. 

Measurements are with a load of 15 pf and an input slew rate of 1 V/ns. 

## **4.5.1.1 SEMC output timing** 

There are ASYNC and SYNC mode for SEMC output timing. 

## **4.5.1.1.1 SEMC output timing in ASYNC mode** 

Table 32 shows SEMC output timing in ASYNC mode. 

## **Table 32. SEMC output timing in ASYNC mode** 

|||||||
|---|---|---|---|---|---|
|**Symbol**|**Parameter**|**Min.**|**Max.**|**Unit**|**Comment**|
||Frequency of operation|—|166|MHz||
|TCK|Internal clock period|6|—|ns||
|TAVO|Address output valid time|—|2|ns|These timing parameters<br>apply to Address and ADV#<br>for NOR/PSRAM in ASYNC<br>mode.|
|TAHO|Address output hold time|(TCK - 2)1|—|ns||
|TADVL|ADV# low time|(TCK - 1)2||||
|TDVO|Data output valid time|—|2|ns|These timing parameters<br>apply to Data/CLE/ALE and<br>WE# for NAND, apply to<br>Data/DM/CRE for<br>NOR/PSRAM, apply to<br>Data/DCX and WRX for DBI<br>interface.|
|TDHO|Data output hold time|(TCK - 2)3|—|ns||
|TWEL|WE# low time|(TCK - 1)4||ns||
|||||||



1 Address output hold time is configurable by SEMC_*CR0.AH. AH field setting value is 0x0 in above table. When AH is set with value N, TAHO min time should be ((N + 1) x TCK). See the _i.MX RT1060 Reference Manual_ (IMXRT1060RM) for more detail about SEMC_*CR0.AH register field. 

**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

NXP Semiconductors 

47 

## **Electrical Characteristics** 

- 2 ADV# low time is configurable by SEMC_*CR0.AS. AS field setting value is 0x0 in above table. When AS is set with value N, TADL min time should be ((N + 1) x TCK - 1). See the _i.MX RT1060 Reference Manual_ (IMXRT1060RM) for more detail about SEMC_*CR0.AS register field. 

- 3 Data output hold time is configurable by SEMC_*CR0.WEH. WEH field setting value is 0x0 in above table. When WEH is set with value N, TDHO min time should be ((N + 1) x TCK). See the _i.MX RT1060 Reference Manual_ (IMXRT1060RM) for more detail about SEMC_*CR0.WEH register field. 

- 4 WE# low time is configurable by SEMC_*CR0.WEL. WEL field setting value is 0x0 in above table. When WEL is set with value N, TWEL min time should be ((N + 1) x TCK - 1). See the _i.MX RT1060 Reference Manual_ (IMXRT1060RM) for more detail about SEMC_*CR0.WEL register field. 

## Figure 15 shows the output timing in ASYNC mode. 

**==> picture [482 x 235] intentionally omitted <==**

**----- Start of picture text -----**<br>
���<br>��������������<br>���� �<br>����<br>���� ����<br>���� �<br>����<br>��� ����<br>**----- End of picture text -----**<br>


## **Figure 15. SEMC output timing in ASYNC mode** 

## **4.5.1.1.2 SEMC output timing in SYNC mode** 

Table 33 shows SEMC output timing in SYNC mode. 

## **Table 33. SEMC output timing in SYNC mode** 

|**Symbol**|**Parameter**|**Min.**|**Max.**|**Unit**|**Comment**|
|---|---|---|---|---|---|
||Frequency of operation|—|166|MHz|—|
|TCK|Internal clock period|6|—|ns|—|
|TDVO|Data output valid time|—|1|ns|These timing parameters apply to<br>Address/Data/DM/CKE/control<br>signals with SEMC_CLK for<br>SDRAM.|
|TDHO|Data output hold time|-1|—|ns||



**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

48 

NXP Semiconductors 

**Electrical Characteristics** 

Figure 16 shows the output timing in SYNC mode. 

**==> picture [227 x 89] intentionally omitted <==**

**----- Start of picture text -----**<br>
��������<br>���� ����<br>���� �<br>**----- End of picture text -----**<br>


## **Figure 16. SEMC output timing in SYNC mode** 

## **4.5.1.2 SEMC input timing** 

There are ASYNC and SYNC mode for SEMC input timing. 

## **4.5.1.2.1 SEMC input timing in ASYNC mode** 

## Table 34 shows SEMC output timing in ASYNC mode. 

## **Table 34. SEMC output timing in ASYNC mode** 

|**Symbol**|**Parameter**|**Min.**|**Max.**|**Unit**|**Comment**|
|---|---|---|---|---|---|
|TIS|Data input setup|8.67|—|ns|For NAND/NOR/PSRAM/DBI,<br>these timing parameters apply<br>to RE# and Read Data.|
|TIH|Data input hold|0|—|ns||



## Figure 17 shows the input timing in ASYNC mode. 

**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

NXP Semiconductors 

49 

**Electrical Characteristics** 

**==> picture [428 x 274] intentionally omitted <==**

**----- Start of picture text -----**<br>
NAND non-EDO mode and NOR/PSRAM/8080 timing<br>OFE<br>DATA LD 11<br>TIS<br>alH<br>NAND EDO mode:timing<br>OE#<br>DATA DO D1<br>TIS alH<br>**----- End of picture text -----**<br>


**Figure 17. SEMC input timing in ASYNC mode** 

## **4.5.1.2.2 SEMC input timing in SYNC mode** 

Table 35 and Table 36 show SEMC input timing in SYNC mode. 

## **Table 35. SEMC input timing in SYNC mode (SEMC_MCR.DQSMD = 0x0)** 

|**Symbol**|**Parameter**|**Min.**|**Max.**|**Unit**|**Comment**|
|---|---|---|---|---|---|
|TIS|Data input setup|8.67|—|ns|—|
|TIH|Data input hold|0|—|ns||



**Table 36. SEMC input timing in SYNC mode (SEMC_MCR.DQSMD = 0x1)** 

|**Symbol**|**Parameter**|**Min.**|**Max.**|**Unit**|**Comment**|
|---|---|---|---|---|---|
|TIS|Data input setup|0.6|—|ns|—|
|TIH|Data input hold|1|—|ns||



Figure 18 shows the input timing in SYNC mode. 

**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

50 

NXP Semiconductors 

**Electrical Characteristics** 

**==> picture [231 x 124] intentionally omitted <==**

**----- Start of picture text -----**<br>
��������<br>���� ��<br>�������� ���<br>���<br>**----- End of picture text -----**<br>


## **Figure 18. SEMC input timing in SYNC mode** 

## **4.5.2 FlexSPI parameters** 

Measurements are with a load 15 pf and input slew rate of 1 V/ns. 

## **4.5.2.1 FlexSPI input/read timing** 

There are four sources for the internal sample clock for FlexSPI read data: 

- Dummy read strobe generated by FlexSPI controller and looped back internally (FlexSPI _n_ _MCR0[RXCLKSRC] = 0x0) 

- Dummy read strobe generated by FlexSPI controller and looped back through the DQS pad (FlexSPI _n_ _MCR0[RXCLKSRC] = 0x1) 

- Read strobe provided by memory device and input from DQS pad (FlexSPI _n_ _MCR0[RXCLKSRC] = 0x3) 

The following sections describe input signal timing for each of these four internal sample clock sources. 

## **4.5.2.1.1 SDR mode with FlexSPI** _**n**_ **_MCR0[RXCLKSRC] = 0x0, 0x1** 

## **Table 37. FlexSPI input timing in SDR mode where FlexSPI** _**n**_ **_MCR0[RXCLKSRC] = 0X0** 

|**Symbol**|**Parameter**|**Min**|**Max**|**Unit**|
|---|---|---|---|---|
||Frequency of operation|—|60|MHz|
|TIS|Setup time for incoming data|8.67|—|ns|
|TIH|Hold time for incoming data|0|—|ns|



## **Table 38. FlexSPI input timing in SDR mode where FlexSPI** _**n**_ **_MCR0[RXCLKSRC] = 0X1** 

|**Symbol**|**Parameter**|**Min**|**Max**|**Unit**|
|---|---|---|---|---|
||Frequency of operation|—|133|MHz|
|TIS|Setup time for incoming data|2|—|ns|
|TIH|Hold time for incoming data|1|—|ns|



**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

NXP Semiconductors 

51 

## **Electrical Characteristics** 

**==> picture [474 x 85] intentionally omitted <==**

**----- Start of picture text -----**<br>
Flexspi input timing in SDR mode<br>0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24<br>SCK a e<br>setup time hold time clock delay<br>SIO[0:7] b DATA0 DATA1 DATA2<br>c<br>internal Sample Clock d<br>**----- End of picture text -----**<br>


## **Figure 19. FlexSPI input timing in SDR mode where FlexSPI** _**n**_ **_MCR0[RXCLKSRC] = 0X0, 0X1** 

## **NOTE** 

Timing shown is based on the memory generating read data on the SCK falling edge, and FlexSPI controller sampling read data on the falling edge. 

## **4.5.2.1.2 SDR mode with FlexSPI** _**n**_ **_MCR0[RXCLKSRC] = 0x3** 

There are two cases when the memory provides both read data and the read strobe in SDR mode: 

- A1—Memory generates both read data and read strobe on SCK rising edge (or falling edge) 

- A2—Memory generates read data on SCK falling edge and generates read strobe on SCK rising edgeSCK rising edge 

**Table 39. FlexSPI input timing in SDR mode where FlexSPI** _**n**_ **_MCR0[RXCLKSRC] = 0x3 (case A1)** 

|**Symbol**|**Parameter**|**Value**|**Value**|**Unit**|
|---|---|---|---|---|
|||**Min**|**Max**||
||Frequency of operation|—|166|MHz|
|TSCKD|Time from SCK to data valid|—|—|ns|
|TSCKDQS|Time from SCK to DQS|—|—|ns|
|TSCKD -TSCKDQS|Time delta between TSCKDand TSCKDQS|-2|2|ns|



**==> picture [467 x 89] intentionally omitted <==**

**----- Start of picture text -----**<br>
SCK<br>TSCKD TSCKD<br>SIO[0:7]<br>TSCKDQS TSCKDQS<br>DQS<br>**----- End of picture text -----**<br>


## **Figure 20. FlexSPI input timing in SDR mode where FlexSPI** _**n**_ **_MCR0[RXCLKSRC] = 0X3 (case A1)** 

**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

52 

NXP Semiconductors 

**Electrical Characteristics** 

## **NOTE** 

Timing shown is based on the memory generating read data and read strobe on the SCK rising edge. The FlexSPI controller samples read data on the DQS falling edge. 

**Table 40. FlexSPI input timing in SDR mode where FlexSPI** _**n**_ **_MCR0[RXCLKSRC] = 0x3 (case A2)** 

|**Symbol**|**Parameter**|**Value**|**Value**|**Unit**|
|---|---|---|---|---|
|||**Min**|**Max**||
||Frequency of operation|—|166|MHz|
|TSCKD|Time from SCK to data valid|—|—|ns|
|TSCKDQS|Time from SCK to DQS|—|—|ns|
|TSCKD -TSCKDQS|Time delta between TSCKDand TSCKDQS|-2|2|ns|



**==> picture [437 x 69] intentionally omitted <==**

**----- Start of picture text -----**<br>
SCK<br>TSCKD TSCKD TSCKD<br>SIO[0:7]<br>TSCKDQS TSCKDQS TSCKDQS<br>DQS<br>**----- End of picture text -----**<br>


Internal Sample Clock 

## **Figure 21. FlexSPI input timing in SDR mode where FlexSPI** _**n**_ **_MCR0[RXCLKSRC] = 0X3 (case A2)** 

## **NOTE** 

Timing shown is based on the memory generating read data on the SCK falling edge and read strobe on the SCK rising edge. The FlexSPI controller samples read data on a half cycle delayed DQS falling edge. 

## **4.5.2.1.3 DDR mode with FlexSPI** _**n**_ **_MCR0[RXCLKSRC] = 0x0, 0x1** 

## **Table 41. FlexSPI input timing in DDR mode where FlexSPI** _**n**_ **_MCR0[RXCLKSRC] = 0x0** 

|**Symbol**|**Parameter**|**Min**|**Max**|**Unit**|
|---|---|---|---|---|
||Frequency of operation|—|30|MHz|
|TIS|Setup time for incoming data|8.67|—|ns|
|TIH|Hold time for incoming data|0|—|ns|



**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

NXP Semiconductors 

53 

**Electrical Characteristics** 

## **Table 42. FlexSPI input timing in DDR mode where FlexSPI** _**n**_ **_MCR0[RXCLKSRC] = 0x1** 

|**Symbol**|**Parameter**|**Min**|**Max**|**Unit**|
|---|---|---|---|---|
||Frequency of operation|—|66|MHz|
|TIS|Setup time for incoming data|2|—|ns|
|TIH|Hold time for incoming data|1|—|ns|



**==> picture [485 x 81] intentionally omitted <==**

**----- Start of picture text -----**<br>
SCLK<br>TIS TIH TIS TIH<br>SIO[0:7]<br>Internal Sample Clock<br>**----- End of picture text -----**<br>


## **Figure 22. FlexSPI input timing in DDR mode where FlexSPI** _**n**_ **_MCR0[RXCLKSRC] = 0x0, 0x1** 

## **4.5.2.1.4 DDR mode with FlexSPI** _**n**_ **_MCR0[RXCLKSRC] = 0x3** 

There are two cases when the memory provides both read data and the read strobe in DDR mode: 

- B1—Memory generates both read data and read strobe on SCK edge 

- B2—Memory generates read data on SCK edge and generates read strobe on SCK2 edge 

**Table 43. FlexSPI input timing in DDR mode where FlexSPI** _**n**_ **_MCR0[RXCLKSRC] = 0x3 (case B1)** 

|**Symbol**|**Parameter**|**Min**|**Max**|**Unit**|
|---|---|---|---|---|
||Frequency of operation|—|166|MHz|
|TSCKD|Time from SCK to data valid|—|—|ns|
|TSCKDQS|Time from SCK to DQS|—|—|ns|
|TSCKD -TSCKDQS|Time delta between TSCKDand TSCKDQS|-1|1|ns|



**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

54 

NXP Semiconductors 

**Electrical Characteristics** 

**==> picture [489 x 89] intentionally omitted <==**

**----- Start of picture text -----**<br>
SCK<br>TSCKD<br>SIO[0:7]<br>TSCKDQS<br>DQS<br>**----- End of picture text -----**<br>


**Figure 23. FlexSPI input timing in DDR mode where FlexSPI** _**n**_ **_MCR0[RXCLKSRC] = 0x3 (case B1)** 

**Table 44. FlexSPI input timing in DDR mode where FlexSPI** _**n**_ **_MCR0[RXCLKSRC] = 0x3 (case B2)** 

|**Symbol**|**Parameter**|**Min**|**Max**|**Unit**|
|---|---|---|---|---|
||Frequency of operation|—|166|MHz|
|TSCKD|Time from SCK to data valid|—|—|ns|
|TSCKD -TSCKDQS|Time delta between TSCKDand TSCKDQS|-1|1|ns|



SCK TSCKD SIO[0:7] SCK2 TSCK2DQS DQS 

**Figure 24. FlexSPI input timing in DDR mode where FlexSPI** _**n**_ **_MCR0[RXCLKSRC] = 0x3 (case B2)** 

## **4.5.2.2 FlexSPI output/write timing** 

The following sections describe output signal timing for the FlexSPI controller including control signals and data outputs. 

## **4.5.2.2.1 SDR mode** 

**Table 45. FlexSPI output timing in SDR mode** 

|**Symbol**|**Parameter**|**Min**|**Max**|**Unit**|
|---|---|---|---|---|
||Frequency of operation|—|1661|MHz|
|Tck|SCK clock period|6.0|—|ns|
|TDVO|Output data valid time|—|1|ns|
|TDHO|Output data hold time|-1|—|ns|



**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

NXP Semiconductors 

55 

## **Electrical Characteristics** 

**Table 45. FlexSPI output timing in SDR mode (continued)** 

|**Symbol**|**Parameter**|**Min**|**Max**|**Unit**|
|---|---|---|---|---|
|TCSS|Chip select output setup time|3 x TCK- 1|—|ns|
|TCSH|Chip select output hold time|3 x TCK+ 2|—|ns|



1 

The actual maximum frequency supported is limited by the FlexSPI _n_ _MCR0[RXCLKSRC] configuration used. Please refer to the FlexSPI SDR input timing specifications. 

## **NOTE** 

TCSS and TCSH are configured by the FlexSPI _n_ _FLSHA _x_ CR1 register, the default values are shown above. See more details in the _i.MX RT1060 Reference Manual (_ IMXRT1060RM _)_ . 

**==> picture [458 x 91] intentionally omitted <==**

**----- Start of picture text -----**<br>
SCK<br>T CSS T CK TCSH<br>CS<br>TDVO TDVO<br>SIO[0:7]<br>TDHO TDHO<br>**----- End of picture text -----**<br>


**Figure 25. FlexSPI output timing in SDR mode** 

## **4.5.2.2.2 SDR mode** 

**Table 46. FlexSPI output timing in SDR mode** 

|**Symbol**|**Parameter**|**Min**|**Max**|**Unit**|
|---|---|---|---|---|
||Frequency of operation1|—|166|MHz|
|Tck|SCK clock period (FlexSPI_n__MCR0[RXCLKSRC] = 0x0)|6.0|—|ns|
|TDVO|Output data valid time|—|2.2|ns|
|TDHO|Output data hold time|0.8|—|ns|
|TCSS|Chip select output setup time|3 x TCK/2 - 0.7|—|ns|
|TCSH|Chip select output hold time|3 x TCK/2 + 0.8|—|ns|
|1|||||
|The actual maximum frequency supported is limited by the FlexSPI_n__MCR0[RXCLKSRC] configuration used. Please refer to the FlexSPI SDR input timing<br>specifications.|||||



## **NOTE** 

TCSS and TCSH are configured by the FlexSPI _n_ _FLSHA _x_ CR1 register, the default values are shown above. See more details in the _i.MX RT1060 Reference Manual (_ IMXRT1060RM _)_ . 

**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

56 

NXP Semiconductors 

**Electrical Characteristics** 

**==> picture [465 x 98] intentionally omitted <==**

**----- Start of picture text -----**<br>
SCK<br>T CSS T CK TCSH<br>CS<br>TDVO TDVO<br>SIO[0:7]<br>TDHO TDHO<br>**----- End of picture text -----**<br>


**Figure 26. FlexSPI output timing in DDR mode** 

## **4.6 Display and graphics** 

The following sections provide information on display and graphic interfaces. 

## **4.6.1 CMOS Sensor Interface (CSI) timing parameters** 

The following sections describe the CSI timing in gated and ungated clock modes. 

## **4.6.1.0.1 Gated clock mode timing** 

Figure 27 and Figure 28 shows the gated clock mode timings for CSI, and Table 47 describes the timing parameters (P1–P7) shown in the figures. A frame starts with a rising/falling edge on CSI_VSYNC (VSYNC), then CSI_HSYNC (HSYNC) is asserted and holds for the entire line. The pixel clock, CSI_PIXCLK (PIXCLK), is valid as long as HSYNC is asserted. 

**==> picture [314 x 198] intentionally omitted <==**

**----- Start of picture text -----**<br>
CSI_VSYNC<br>P1<br>CSI_HSYNC<br>P7<br>P2<br>P5 P6<br>CSI_PIXCLK<br>P3 P4<br>CSI_DATA[23:00]<br>**----- End of picture text -----**<br>


**Figure 27. CSI Gated clock mode—sensor data at falling edge, latch data at rising edge** 

**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

NXP Semiconductors 

57 

**Electrical Characteristics** 

**==> picture [299 x 189] intentionally omitted <==**

**----- Start of picture text -----**<br>
CSI_VSYNC<br>P1<br>CSI_HSYNC<br>P7<br>P2<br>P6 P5<br>CSI_PIXCLK<br>P3 P4<br>CSI_DATA[23:00]<br>**----- End of picture text -----**<br>


**Figure 28. CSI Gated clock mode—sensor data at rising edge, latch data at falling edge** 

**Table 47. CSI gated clock mode timing parameters** 

|**ID**|**Parameter**|**Symbol**|**Min.**|**Max.**|**Units**|
|---|---|---|---|---|---|
|P1|CSI_VSYNC to CSI_HSYNC time|tV2H|33.5|—|ns|
|P2|CSI_HSYNC setup time|tHsu|1|—|ns|
|P3|CSI DATA setup time|tDsu|1|—|ns|
|P4|CSI DATA hold time|tDh|1|—|ns|
|P5|CSI pixel clock high time|tCLKh|3.75|—|ns|
|P6|CSI pixel clock low time|tCLKl|3.75|—|ns|
|P7|CSI pixel clock frequency|fCLK|—|80|MHz|



**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

58 

NXP Semiconductors 

**Electrical Characteristics** 

## **4.6.1.0.2 Ungated clock mode timing** 

Figure 29 shows the ungated clock mode timings of CSI, and Table 48 describes the timing parameters (P1–P6) that are shown in the figure. In ungated mode the CSI_VSYNC and CSI_PIXCLK signals are used, and the CSI_HSYNC signal is ignored. 

**==> picture [314 x 159] intentionally omitted <==**

**----- Start of picture text -----**<br>
CSI_VSYNC<br>P1<br>P6<br>P4 P5<br>CSI_PIXCLK<br>P2 P3<br>CSI_DATA[23:00]<br>**----- End of picture text -----**<br>


**Figure 29. CSI ungated clock mode—sensor data at falling edge, latch data at rising edge** 

**Table 48. CSI ungated clock mode timing parameters** 

|**ID**|**Parameter**|**Symbol**|**Min.**|**Max.**|**Units**|
|---|---|---|---|---|---|
|P1|CSI_VSYNC to pixel clock time|tVSYNC|33.5|—|ns|
|P2|CSI DATA setup time|tDsu|1|—|ns|
|P3|CSI DATA hold time|tDh|1|—|ns|
|P4|CSI pixel clock high time|tCLKh|3.75|—|ns|
|P5|CSI pixel clock low time|tCLKl|3.75|—|ns|
|P6|CSI pixel clock frequency|fCLK|—|80|MHz|



The CSI enables the chip to connect directly to external CMOS image sensors, which are classified as dumb or smart as follows: 

- Dumb sensors only support traditional sensor timing (vertical sync (VSYNC) and horizontal sync (HSYNC)) and output-only Bayer and statistics data. 

- Smart sensors support CCIR656 video decoder formats and perform additional processing of the image (for example, image compression, image pre-filtering, and various data output formats). 

**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

NXP Semiconductors 

59 

**Electrical Characteristics** 

## **4.6.2 LCD Controller (LCDIF) timing parameters** 

Figure 30 shows the LCDIF timing and Table 49 lists the timing parameters. 

**==> picture [494 x 365] intentionally omitted <==**

**----- Start of picture text -----**<br>
L1 L2 L3<br>LCDn_CLK<br>(falling edge capture)<br>LCDn_CLK<br>(rising edge capture)<br>LCDn_DATA[23:00]<br>LCDn Control Signals<br>L4<br>L5<br>L6<br>L7<br>Figure 30. LCD timing<br>Table 49. LCD timing parameters<br>ID Parameter Symbol Min Max Unit<br>L1 LCD pixel clock frequency tCLK(LCD) — 75 MHz<br>L2 LCD pixel clock high (falling edge capture) tCLKH(LCD) 3 — ns<br>L3 LCD pixel clock low (rising edge capture) tCLKL(LCD) 3 — ns<br>L4 LCD pixel clock high to data valid (falling edge capture) td(CLKH-DV) -1 1 ns<br>L5 LCD pixel clock low to data valid (rising edge capture) td(CLKL-DV) -1 1 ns<br>L6 LCD pixel clock high to control signal valid (falling edge capture) td(CLKH-CTRLV) -1 1 ns<br>L7 LCD pixel clock low to control signal valid (rising edge capture) td(CLKL-CTRLV) -1 1 ns<br>**----- End of picture text -----**<br>


## **4.7 Audio** 

This section provide information about SAI/I2S and SPDIF. 

## **4.7.1 SAI/I2S switching specifications** 

This section provides the AC timings for the SAI in master (clocks driven) and slave (clocks input) modes. All timings are given for non-inverted serial clock polarity (SAI_TCR[TSCKP] = 0, SAI_RCR[RSCKP] = 0) and non-inverted frame sync (SAI_TCR[TFSI] = 0, SAI_RCR[RFSI] = 0). If the polarity of the clock and/or the frame sync have been inverted, all the timings remain valid by inverting the clock signal (SAI_BCLK) and/or the frame sync (SAI_FS) shown in the figures below. 

**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

60 

NXP Semiconductors 

**Electrical Characteristics** 

## **Table 50. Master mode SAI timing** 

|**Num**|**Characteristic**|**Min**|**Max**|**Unit**|
|---|---|---|---|---|
|S1|SAI_MCLK cycle time|15|—|ns|
|S2|SAI_MCLK pulse width high/low|40%|60%|MCLK period|
|S3|SAI_BCLK cycle time|40|—|ns|
|S4|SAI_BCLK pulse width high/low|40%|60%|BCLK period|
|S5|SAI_BCLK to SAI_FS output valid|—|15|ns|
|S6|SAI_BCLK to SAI_FS output invalid|0|—|ns|
|S7|SAI_BCLK to SAI_TXD valid|—|15|ns|
|S8|SAI_BCLK to SAI_TXD invalid|0|—|ns|
|S9|SAI_RXD/SAI_FS input setup before SAI_BCLK|15|—|ns|
|S10|SAI_RXD/SAI_FS input hold after SAI_BCLK|0|—|ns|



**==> picture [499 x 200] intentionally omitted <==**

**Figure 31. SAI timing—Master modes** 

## **Table 51. Slave mode SAI timing** 

|**Num**|**Characteristic**|**Min**|**Max**|**Unit**|
|---|---|---|---|---|
|S11|SAI_BCLK cycle time (input)|40|—|ns|
|S12|SAI_BCLK pulse width high/low (input)|40%|60%|BCLK period|
|S13|SAI_FS input setup before SAI_BCLK|10|—|ns|
|S14|SAI_FA input hold after SAI_BCLK|2|—|ns|
|S15|SAI_BCLK to SAI_TXD/SAI_FS output valid|—|20|ns|
|S16|SAI_BCLK to SAI_TXD/SAI_FS output invalid|0|—|ns|



**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

NXP Semiconductors 

61 

**Electrical Characteristics** 

## **Table 51. Slave mode SAI timing** 

**==> picture [508 x 59] intentionally omitted <==**

**----- Start of picture text -----**<br>
Num Characteristic Min Max Unit<br>S17 SAI_RXD setup before SAI_BCLK 10 — ns<br>S18 SAI_RXD hold after SAI_BCLK 2 — ns<br>**----- End of picture text -----**<br>


**==> picture [492 x 181] intentionally omitted <==**

**Figure 32. SAI timing—Slave mode** 

## **4.7.2 SPDIF timing parameters** 

The Sony/Philips Digital Interconnect Format (SPDIF) data is sent using the bi-phase marking code. When encoding, the SPDIF data signal is modulated by a clock that is twice the bit rate of the data signal. 

Table 52 and Figure 33 and Figure 34 show SPDIF timing parameters for the Sony/Philips Digital Interconnect Format (SPDIF), including the timing of the modulating Rx clock (SPDIF_SR_CLK) for SPDIF in Rx mode and the timing of the modulating Tx clock (SPDIF_ST_CLK) for SPDIF in Tx mode. 

## **Table 52. SPDIF timing parameters** 

|**Characteristics**|**Symbol**|**Timing Parameter Range**|**Timing Parameter Range**|**Unit**|
|---|---|---|---|---|
|||**Min**|**Max**||
|SPDIF_IN Skew: asynchronous inputs, no specs apply|—|—|0.7|ns|
|SPDIF_OUT output (Load = 50pf)<br>• Skew<br>• Transition rising<br>• Transition falling|—<br>—<br>—|—<br>—<br>—|1.5<br>24.2<br>31.3|ns|
|SPDIF_OUT1 output (Load = 30pf)<br>• Skew<br>• Transition rising<br>• Transition falling|—<br>—<br>—|—<br>—<br>—|1.5<br>13.6<br>18.0|ns|
|Modulating Rx clock (SPDIF_SR_CLK) period|srckp|40.0|—|ns|



**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

62 

NXP Semiconductors 

**Electrical Characteristics** 

**==> picture [502 x 367] intentionally omitted <==**

**----- Start of picture text -----**<br>
Table 52. SPDIF timing parameters (continued)<br>Timing Parameter Range<br>Characteristics Symbol Unit<br>Min Max<br>SPDIF_SR_CLK high period srckph 16.0 — ns<br>SPDIF_SR_CLK low period srckpl 16.0 — ns<br>Modulating Tx clock (SPDIF_ST_CLK) period stclkp 40.0 — ns<br>SPDIF_ST_CLK high period stclkph 16.0 — ns<br>SPDIF_ST_CLK low period stclkpl 16.0 — ns<br>srckp<br>srckpl srckph<br>SPDIF_SR_CLK<br>VM VM<br>(Output)<br>Figure 33. SPDIF_SR_CLK timing diagram<br>stclkp<br>stclkpl stclkph<br>SPDIF_ST_CLK<br>VM VM<br>(Input)<br>**----- End of picture text -----**<br>


**Figure 34. SPDIF_ST_CLK timing diagram** 

## **4.8 Analog** 

The following sections provide information about analog interfaces. 

## **4.8.1 DCDC** 

Table 53 introduces the DCDC electrical specifications. 

**Table 53. DCDC electrical specifications** 

|**Mode**|**Buck mode, one output**|**Notes**|
|---|---|---|
|Input voltage|3.3 V|Min = 2.8 V, Max = 3.6 V|
|Output voltage|1.1 V|Configurable 0.8 - 1.575 with 25 mV one step<br>in Run mode|
|Max loading|500 mA|—|
|Loading in low power modes|200A ~ 30 mA|—|



**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

NXP Semiconductors 

63 

**Electrical Characteristics** 

**Table 53. DCDC electrical specifications (continued)** 

|**Mode**|**Buck mode, one output**|**Notes**|
|---|---|---|
|Efficiency|90% max|@150 mA|
|Low power mode|Open loop mode|Ripple is about 15 mV in Run mode|
|Run mode|• Always continuous mode<br>• Support discontinuous mode|Configurable by register|
|Inductor|4.7H|—|
|Capacitor|33F|—|
|Over voltage protection|1.55 V|Detect VDDSOC, when the voltage is higher<br>than 1.6 V, shutdown DCDC.|
|Over Current protection|1 A|Detect the peak current<br>• Run mode: when the current is larger than<br>1 A, shutdown DCDC.|
|Low DCDC_IN detection|2.6 V|Detect the DCDC_IN, when battery is lower<br>than 2.6 V, shutdown DCDC.|



## **4.8.2 A/D converter** 

This section introduces information about A/D converter. 

## **4.8.2.1 12-bit ADC electrical characteristics** 

The section provide information about 12-bit ADC electrical characteristics. 

## **4.8.2.1.1 12-bit ADC operating conditions** 

## **Table 54. 12-bit ADC operating conditions** 

|**Characteristic**|**Conditions**|**Symb**|**Min**|**Typ1**|**Max**|**Unit**|**Comment**|
|---|---|---|---|---|---|---|---|
|Supply voltage|Absolute|VDDA|3.0|-|3.6|V|—|
||Delta to<br>VDDA_ADC_3P3<br>(VDD-VDDA)2|VDDA|-100|0|100|mV|—|
|Ground voltage|Delta to VSS<br>(VSS-VSSAD)|VSSAD|-100|0|100|mV|—|
|Ref Voltage High|—|VDDA|1.13|VDDA|VDDA|V|—|
|Ref Voltage Low|—|VSS|VSS|VSS|VSS|V|—|
|Input Voltage|—|VADIN|VSS|—|VDDA|V|—|
|Input Capacitance|8/10/12 bit modes|CADIN|—|1.5|2|pF|—|
|Input Resistance|ADLPC=0, ADHSC=1|RADIN|—|5|7|kohms|—|
||ADLPC=0, ADHSC=0||—|12.5|15|kohms|—|
||ADLPC=1, ADHSC=0||—|25|30|kohms|—|



**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

64 

NXP Semiconductors 

**Electrical Characteristics** 

**Table 54. 12-bit ADC operating conditions (continued)** 

|**Characteristic**|**Conditions**|**Symb**||**Min**||**Typ1**||**Max**|**Unit**|**Comment**|
|---|---|---|---|---|---|---|---|---|---|---|
|Analog Source|12 bit mode fADCK=|RAS|—||—||1||kohms|Tsamp=150|
|Resistance|40MHz ADLSMP=0,|||||||||ns|
||ADSTS=10, ADHSC=1||||||||||



RAS depends on Sample Time Setting (ADLSMP, ADSTS) and ADC Power Mode (ADHSC, ADLPC). See charts for Minimum Sample Time vs RAS 

|<br>Sample Time vs RAS||||||||
|---|---|---|---|---|---|---|---|
|ADC Conversion Clock|ADLPC=0, ADHSC=1|fADCK|4|—|40|MHz|—|
|Frequency|12 bit mode|||||||
||ADLPC=0, ADHSC=0||4|—|30|MHz|—|
||12 bit mode|||||||
||ADLPC=1, ADHSC=0||4|—|20|MHz|—|
||12 bit mode|||||||



1 Typical values assume VDDAD = 3.0 V, Temp = 25°C, fADCK=20 MHz unless otherwise stated. Typical values are for reference only and are not tested in production. 

2 DC potential differences 

**==> picture [458 x 319] intentionally omitted <==**

**Figure 35. 12-bit ADC input impedance equivalency diagram** 

**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

NXP Semiconductors 

65 

**Electrical Characteristics** 

## **12-bit ADC characteristics** 

**Table 55. 12-bit ADC characteristics (VREFH = VDDA, VREFL = VSSAD)** 

|**Characteristic**|**Conditions1**|**Symb**|**Min**|**Typ2**|**Max**|**Unit**|**Comment**|
|---|---|---|---|---|---|---|---|
|Supply Current|ADLPC=1,<br>ADHSC=0|IDDA|—|350|—|µA|ADLSMP=0<br>ADSTS=10 ADCO=1|
||ADLPC=0,<br>ADHSC=0|||460||||
||ADLPC=0,<br>ADHSC=1|||750||||
|Supply Current|Stop, Reset, Module<br>Off|IDDA|—|1.4|2|µA|—|
|ADC Asynchronous<br>Clock Source|ADHSC=0|fADACK|—|10|—|MHz|tADACK= 1/fADACK|
||ADHSC=1||—|20|—|||
|Sample Cycles|ADLSMP=0,<br>ADSTS=00|Csamp|—|2|—|cycles|—|
||ADLSMP=0,<br>ADSTS=01|||4||||
||ADLSMP=0,<br>ADSTS=10|||6||||
||ADLSMP=0,<br>ADSTS=11|||8||||
||ADLSMP=1,<br>ADSTS=00|||12||||
||ADLSMP=1,<br>ADSTS=01|||16||||
||ADLSMP=1,<br>ADSTS=10|||20||||
||ADLSMP=1,<br>ADSTS=11|||24||||



**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

66 

NXP Semiconductors 

**Electrical Characteristics** 

**Table 55. 12-bit ADC characteristics (VREFH = VDDA, VREFL = VSSAD) (continued)** 

|**Characteristic**|**Conditions1**|**Symb**|**Min**|**Typ2**|**Max**|**Unit**|**Comment**|
|---|---|---|---|---|---|---|---|
|Conversion Cycles|ADLSMP=0<br>ADSTS=00|Cconv|—|28|—|cycles|—|
||ADLSMP=0<br>ADSTS=01|||30||||
||ADLSMP=0<br>ADSTS=10|||32||||
||ADLSMP=0<br>ADSTS=11|||34||||
||ADLSMP=1<br>ADSTS=00|||38||||
||ADLSMP=1<br>ADSTS=01|||42||||
||ADLSMP=1<br>ADSTS=10|||46||||
||ADLSMP=1,<br>ADSTS=11|||50||||
|Conversion Time|ADLSMP=0<br>ADSTS=00|Tconv|—|0.7|—|µs|Fadc=40 MHz|
||ADLSMP=0<br>ADSTS=01|||0.75||||
||ADLSMP=0<br>ADSTS=10|||0.8||||
||ADLSMP=0<br>ADSTS=11|||0.85||||
||ADLSMP=1<br>ADSTS=00|||0.95||||
||ADLSMP=1<br>ADSTS=01|||1.05||||
||ADLSMP=1<br>ADSTS=10|||1.15||||
||ADLSMP=1,<br>ADSTS=11|||1.25||||
|Total Unadjusted<br>Error|12 bit mode|TUE|—|3.4|4.28|LSB<br>1 LSB =<br>(VREFH-<br>VREFL)/2<br>N|AVGE = 1, AVGS =<br>11|
||10 bit mode||—|1.5|1.95|||
||8 bit mode||—|1.2|1.25|||
|Differential<br>Non-Linearity|12 bit mode|DNL|—|0.76|1.29|LSB|AVGE = 1, AVGS =<br>11|
||10bit mode||—|0.36|0.72|||
||8 bit mode||—|0.14|0.15|||



**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

NXP Semiconductors 

67 

## **Electrical Characteristics** 

**Table 55. 12-bit ADC characteristics (VREFH = VDDA, VREFL = VSSAD) (continued)** 

|**Characteristic**|**Conditions1**|**Symb**|**Min**|**Typ2**|**Max**|**Unit**|**Comment**|
|---|---|---|---|---|---|---|---|
|Integral<br>Non-Linearity|12 bit mode|INL|—|2.78|4.01|LSB|AVGE = 1, AVGS =<br>11|
||10bit mode||—|0.61|1.01|||
||8 bit mode||—|0.14|0.29|||
|Offset Error3|12 bit mode|EO|—|-0.03|-0.07|%FSV|AVGE = 1, AVGS =<br>11|
||10bit mode||—|-0.03|-0.10|||
||8 bit mode||—|-0.08|-0.14|||
|Gain Error4|12 bit mode|Eg|—|0.01|0.03|%FSV|AVGE = 1, AVGS =<br>11|
||10bit mode||—|0.03|0.06|||
||8 bit mode||—|0.07|0.15|||
|Effective Number of<br>Bits|12 bit mode|ENOB|10.1|10.7|—|Bits|AVGE = 1, AVGS =<br>11|
|Signal to Noise plus<br>Distortion|See ENOB|SINAD|SINAD = 6.02 x ENOB + 1.76|||dB|AVGE = 1, AVGS =<br>11|



1 All accuracy numbers assume the ADC is calibrated with VREFH = VDDAD 

- 2 Typical values assume VDDAD = 3.0 V, Temp = 25°C, Fadck = 20 MHz unless otherwise stated. Typical values are for reference only and are not tested in production. 

3 Offset error is same as ZSE, error measured at 0 V with zero scale. 

4 Gain error is FSE-ZSE (same as FSE-EO). 

## **NOTE** 

## The ADC electrical spec is met with the calibration enabled configuration. 

**==> picture [328 x 163] intentionally omitted <==**

**Figure 36. Minimum Sample Time Vs Ras (Cas = 2pF)** 

**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

68 

NXP Semiconductors 

**Electrical Characteristics** 

**==> picture [330 x 162] intentionally omitted <==**

**Figure 37. Minimum Sample Time Vs Ras (Cas = 5 pF)** 

**==> picture [324 x 163] intentionally omitted <==**

**Figure 38. Minimum Sample Time Vs Ras (Cas = 10 pF)** 

## **4.8.3 ACMP** 

Table 56 lists the ACMP electrical specifications. 

**Table 56. Comparator and 6-bit DAC electrical specifications** 

|**Symbol**|**Description**|**Min.**|**Typ.**|**Max.**|**Unit**|
|---|---|---|---|---|---|
|VDD|Supply voltage|3.0|—|3.6|V|
|IDDHS|Supply current, High-speed mode<br>(EN = 1, PMODE = 1)|—|347|—|A|
|IDDLS|Supply current, Low-speed mode<br>(EN = 1, PMODE = 0)|—|42|—|A|
|VAIN|Analog input voltage|VSS|—|VDD|V|
|VAIO|Analog input offset voltage|—|—|21|mV|



**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

NXP Semiconductors 

69 

**Electrical Characteristics** 

**Table 56. Comparator and 6-bit DAC electrical specifications (continued)** 

|**Symbol**|**Description**|**Min.**|**Typ.**|**Max.**|**Unit**|
|---|---|---|---|---|---|
|VH|Analog comparator hysteresis1||||mV|
||• CR0[HYSTCTR] = 00|—|1|2||
||• CR0[HYSTCTR] = 01|—|21|54||
||• CR0[HYSTCTR] = 10|—|42|108||
||• CR0[HYSTCTR] = 11|—|64|184||
|VCMPOH|Output high|VDD- 0.5|—|—|V|
|VCMPOI|Output low|—|—|0.5|V|
|tDHS|Propagation delay, high-speed<br>mode (EN = 1, PMODE = 1)2|—|25|40|ns|
|tDLS|Propagation delay, low-speed<br>mode (EN = 1, PMODE = 0)2|—|50|90|ns|
|tDInit|Analog comparator initialization<br>delay3|—|1.5|—|s|
|IDAC6b|6-bit DAC current adder (enabled)|—|5|—|A|
|RDAC6b|6-bit DAC reference inputs|—|VDD|—|V|
|INLDAC6b|6-bit DAC integral non-linearity|-0.3|—|0.3|LSB4|
|DNLDAC6b|6-bit DAC differential non-linearity|-0.15|—|0.15|LSB4|



1 Typical hysteresis is measured with input voltage range limited to 0.7 to VDD - 0.7 V in high speed mode. 

2 Signal swing is 100 mV. 

3 Comparator initialization delay is defined as the time between software writes to the enable comparator module and the comparator output setting to a stable level. 

4 1 LSB = Vreference / 64 

## **4.9 Communication interfaces** 

The following sections provide the information about communication interfaces. 

## **4.9.1 LPSPI timing parameters** 

The Low Power Serial Peripheral Interface (LPSPI) provides a synchronous serial bus with master and slave operations. Many of the transfer attributes are programmable. The following tables provide timing characteristics for classic LPSPI timing modes. 

All timing is shown with respect to 20% VDD and 80% VDD thresholds, unless noted, as well as input signal transitions of 3 ns and a 30 pF maximum load on all LPSPI pins. 

**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

70 

NXP Semiconductors 

**Electrical Characteristics** 

## **Table 57. LPSPI Master mode timing** 

|**Number**|**Symbol**|**Description**|**Min.**|**Max.**|**Units**|**Note**|
|---|---|---|---|---|---|---|
|1|fSCK|Frequency of operation|—|fperiph/ 2|Hz|1|
|2|tSCK|SCK period|2 x tperiph|—|ns|2|
|3|tLead|Enable lead time|1|—|tperiph|—|
|4|tLag|Enable lag time|1|—|tperiph|—|
|5|tWSCK|Clock (SCK) high or low time|tSCK/ 2 - 3|—|ns|—|
|6|tSU|Data setup time (inputs) with SAMPLE set to<br>0|10|—|ns|3|
|||Data setup time (inputs) with SAMPLE set to<br>1|2.7|—|ns||
|7|tHI|Data hold time (inputs)|2|—|ns|—|
|8|tV|Data valid (after SCK edge)|—|8|ns|—|
|9|tHO|Data hold time (outputs)|0|—|ns|—|



- 1 Absolute maximum frequency of operation (fop) is 30 MHz. The clock driver in the LPSPI module for fperiph must be guaranteed this limit is not exceeded. 

- 2 t = 1 / f periph periph 

- 3 SAMPLE is a bit field in register CFGR1, See the i.MX RT1060 Reference Manual (IMXRT1060RM _)_ for further details. 

**==> picture [465 x 243] intentionally omitted <==**

**----- Start of picture text -----**<br>
PCS [1]<br>(OUTPUT)<br>3 2 4<br>SCK 5<br>(CPOL=0)<br>(OUTPUT) 5<br>SCK<br>(CPOL=1)<br>(OUTPUT)<br>6 7<br>SIN MSB IN [2] BIT 6 . . . 1 LSB IN<br>(INPUT)<br>8 9<br>SOUT<br>(OUTPUT) MSB OUT [2] BIT 6 . . . 1 LSB OUT<br>1. If configured as an output.<br>2. LSBF = 0. For LSBF = 1, bit order is LSB, bit 1, ..., bit 6, MSB.<br>**----- End of picture text -----**<br>


**Figure 39. LPSPI Master mode timing (CPHA = 0)** 

**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

NXP Semiconductors 

71 

## **Electrical Characteristics** 

**==> picture [474 x 216] intentionally omitted <==**

**----- Start of picture text -----**<br>
1<br>PCS<br>(OUTPUT)<br>2<br>3 4<br>SCK<br>(CPOL=0)<br>(OUTPUT)<br>5 5<br>SCK<br>(CPOL=1)<br>(OUTPUT)<br>6 7<br>SIN 2<br>MSB IN BIT 6 . . . 1 LSB IN<br>(INPUT)<br>8 9<br>SOUT 2<br>PORT DATA MASTER MSB OUT BIT 6 . . . 1 MASTER LSB OUT PORT DATA<br>(OUTPUT)<br>**----- End of picture text -----**<br>


1.If configured as output 2. LSBF = 0. For LSBF = 1, bit order is LSB, bit 1, ..., bit 6, MSB. 

## **Figure 40. LPSPI Master mode timing (CPHA = 1)** 

## **Table 58. LPSPI Slave mode timing** 

s 

|**Number**|**Symbol**|**Description**|**Min.**|**Max.**|**Units**|**Note**|
|---|---|---|---|---|---|---|
|1|fSCK|Frequency of operation|0|fperiph/ 2|Hz|1|
|2|tSCK|SCK period|2 x tperiph|—|ns|2|
|3|tLead|Enable lead time|1|—|tperiph|—|
|4|tLag|Enable lag time|1|—|tperiph|—|
|5|tWSCK|Clock (SCK) high or low time|tSCK/ 2 - 5|—|ns|—|
|6|tSU|Data setup time (inputs)|2.7|—|ns|—|
|7|tHI|Data hold time (inputs)|3.8|—|ns|—|
|8|ta|Slave access time|—|tperiph|ns|3|
|9|tdis|Slave MISO disable time|—|tperiph|ns|4|
|10|tV|Data valid (after SCK edge)|—|14.5|ns|—|
|11|tHO|Data hold time (outputs)|0|—|ns|—|



1 Absolute maximum frequency of operation (fop) is 30 MHz. The clock driver in the LPSPI module for fperiph must be guaranteed this limit is not exceeded. 

> 2 t = 1 / f periph periph 

3 Time to data active from high-impedance state 

4 Hold time to high-impedance state 

**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

72 

NXP Semiconductors 

**Electrical Characteristics** 

**==> picture [489 x 538] intentionally omitted <==**

**----- Start of picture text -----**<br>
PCS<br>(INPUT)<br>2 4<br>SCK<br>(CPOL=0)<br>(INPUT)<br>3 5 5<br>SCK<br>(CPOL=1)<br>(INPUT)<br>9<br>8 10 11 11<br>SIN see SEE<br>(OUTPUT) note SLAVE MSB BIT 6 . . . 1 SLAVE LSB OUT NOTE<br>6 7<br>SOUT<br>MSB IN BIT 6 . . . 1 LSB IN<br>(INPUT) NOTE: Not defined<br>Figure 41. LPSPI Slave mode timing (CPHA = 0)<br>PCS<br>(INPUT)<br>2 4<br>3<br>SCK<br>(CPOL=0)<br>(INPUT)<br>5 5<br>SCK<br>(CPOL=1)<br>(INPUT)<br>1 0 1 1 9<br>SIN see<br>SLAVE MSB OUT BIT 6 . . . 1 SLAVE LSB OUT<br>(OUTPUT) note<br>8 6 7<br>SOUT<br>(INPUT) MSB IN BIT 6 . . . 1 LSB IN<br>NOTE: Not defined<br>Figure 42. LPSPI Slave mode timing (CPHA = 1)<br>**----- End of picture text -----**<br>


**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

NXP Semiconductors 

73 

**Electrical Characteristics** 

## **4.9.2 LPI2C module timing parameters** 

This section describes the timing parameters of the LPI2C module. 

## **Table 59. LPI2C module timing parameters** 

|**Symbol**|**Description**|**Description**|**Min**|**Max**|**Unit**|**Notes**|
|---|---|---|---|---|---|---|
|fSCL|SCL clock frequency|Standard mode (Sm)|0|100|kHz|1, 2|
|||Fast mode (Fm)|0|400|||
|||Fast mode Plus (Fm+)|0|1000|||
|||Ultra Fast mode (UFm)|0|5000|||
|||High speed mode (Hs-mode)|0|3400|||



1 Hs-mode is only supported in slave mode. 

2 See General switching specifications. 

## **4.9.3 Ultra High Speed SD/SDIO/MMC Host Interface (uSDHC) AC timing** 

This section describes the electrical information of the uSDHC, which includes SD/eMMC4.3 (Single Data Rate) timing, eMMC4.4/4.41/4.5 (Dual Date Rate) timing and SDR104/50(SD3.0) timing. 

## **4.9.3.1 SD/eMMC4.3 (single data rate) AC timing** 

Figure 43 depicts the timing of SD/eMMC4.3, and Table 60 lists the SD/eMMC4.3 timing characteristics. 

**==> picture [347 x 186] intentionally omitted <==**

**----- Start of picture text -----**<br>
SD4<br>SD2<br>SD1<br>SD5<br>SDx_CLK<br>SD3<br>SD6<br>Output from uSDHC to card<br>SDx_DATA[7:0]<br>SD7 SD8<br>Input from card to uSDHC<br>SDx_DATA[7:0]<br>**----- End of picture text -----**<br>


**Figure 43. SD/eMMC4.3 timing** 

**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

74 

NXP Semiconductors 

**Electrical Characteristics** 

## **Table 60. SD/eMMC4.3 interface timing specification** 

|**ID**|**Parameter**|**Symbols**|**Min**|**Max**|**Unit**|
|---|---|---|---|---|---|
||**Card Input Clock**|||||
|SD1|Clock Frequency (Low Speed)|fPP<br>1|0|400|kHz|
||Clock Frequency (SD/SDIO Full Speed/High Speed)|fPP<br>2|0|25/50|MHz|
||Clock Frequency (MMC Full Speed/High Speed)|fPP<br>3|0|20/52|MHz|
||Clock Frequency (Identification Mode)|fOD|100|400|kHz|
|SD2|Clock Low Time|tWL|7|—|ns|
|SD3|Clock High Time|tWH|7|—|ns|
|SD4|Clock Rise Time|tTLH|—|3|ns|
|SD5|Clock Fall Time|tTHL|—|3|ns|
||**uSDHC Output/Card Inputs SD_CMD, SDx_DATAx (Reference to CLK)**|||||
|SD6|uSDHC Output Delay|tOD|-6.6|3.6|ns|
||**uSDHC Input/Card Outputs SD_CMD, SDx_DATAx (Reference to CLK)**|||||
|SD7|uSDHC Input Setup Time|tISU|2.5|—|ns|
|SD8|uSDHC Input Hold Time4|tIH|1.5|—|ns|



1 In low speed mode, card clock must be lower than 400 kHz, voltage ranges from 2.7 to 3.6 V. 

> 2 – In normal (full) speed mode for SD/SDIO card, clock frequency can be any value between 0 25 MHz. In high-speed mode, clock frequency can be any value between 0–50 MHz. 

- 3 – In normal (full) speed mode for MMC card, clock frequency can be any value between 0 20 MHz. In high-speed mode, clock frequency can be any value between 0–52 MHz. 

4 To satisfy hold timing, the delay difference between clock input and cmd/data input must not exceed 2 ns. 

## **4.9.3.2 eMMC4.4/4.41 (dual data rate) AC timing** 

Figure 44 depicts the timing of eMMC4.4/4.41. Table 61 lists the eMMC4.4/4.41 timing characteristics. Be aware that only DATA is sampled on both edges of the clock (not applicable to CMD). 

**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

NXP Semiconductors 

75 

## **Electrical Characteristics** 

**==> picture [367 x 164] intentionally omitted <==**

**----- Start of picture text -----**<br>
SD1<br>SDx_CLK<br>SD2 SD2<br>Output from eSDHCv3 to cardSDx_DATA[7:0] ......<br>SD3 SD4<br>Input from card to eSDHCv3<br>SDx_DATA[7:0] ......<br>**----- End of picture text -----**<br>


**Figure 44. eMMC4.4/4.41 timing** 

**Table 61. eMMC4.4/4.41 interface timing specification** 

|**ID**|**Parameter**|**Symbols**|**Min**|**Max**|**Unit**|
|---|---|---|---|---|---|
|**Card Input Clock**||||||
|SD1|Clock Frequency (eMMC4.4/4.41 DDR)|fPP|0|52|MHz|
|SD1|Clock Frequency (SD3.0 DDR)|fPP|0|50|MHz|
|**uSDHC Output / Card Inputs SD_CMD, SDx_DATAx (Reference to CLK)**||||||
|SD2|uSDHC Output Delay|tOD|2.5|7.1|ns|
|**uSDHC Input / Card Outputs SD_CMD, SDx_DATAx (Reference to CLK)**||||||
|SD3|uSDHC Input Setup Time|tISU|1.7|—|ns|
|SD4|uSDHC Input Hold Time|tIH|1.5|—|ns|



**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

76 

NXP Semiconductors 

**Electrical Characteristics** 

## **4.9.3.3 SDR50/SDR104 AC timing** 

Figure 45 depicts the timing of SDR50/SDR104, and Table 62 lists the SDR50/SDR104 timing characteristics. 

|SCK<br>4-bit output from uSDHC to card<br>4-bit input from card to uSDHC|||||||SD1|SD1|SD1|SD1|SD1|||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||||||||
|||SD2||||||SD3||||||||||||
|||||||||||||||||||||
|||SD6<br>SD4/SD5||||||||||||||||||
|||||||||||||||||||||
|||||||||||||||||||||
||||||SD6|||||||||||||||
|||||||||SD8||||||||||||
|||||||||||||||||||||
|||||||||||||||||||||
|||||||||||||||||||||



**Figure 45. SDR50/SDR104 timing** 

**Table 62. SDR50/SDR104 interface timing specification** 

|**ID**|**Parameter**|**Symbols**|**Min**|**Max**|**Unit**|
|---|---|---|---|---|---|
|**Card Input Clock**||||||
|SD1|Clock Frequency Period|tCLK|5.0|—|ns|
|SD2|Clock Low Time|tCL|0.46 x tCLK|0.54 x tCLK|ns|
|SD3|Clock High Time|tCH|0.46 x tCLK|0.54 x tCLK|ns|
|**uSDHC Output/Card Inputs SD_CMD, SDx_DATAx in SDR50 (Reference to CLK)**||||||
|SD4|uSDHC Output Delay|tOD|–3|1|ns|
|**uSDHC Output/Card Inputs SD_CMD, SDx_DATAx in SDR104 (Reference to CLK)**||||||
|SD5|uSDHC Output Delay|tOD|–1.6|1|ns|
|**uSDHC Input/Card Outputs SD_CMD, SDx_DATAx in SDR50 (Reference to CLK)**||||||
|SD6|uSDHC Input Setup Time|tISU|2.5|—|ns|
|SD7|uSDHC Input Hold Time|tIH|1.5|—|ns|
|**uSDHC Input/Card Outputs SD_CMD, SDx_DATAx in SDR104 (Reference to CLK)1**||||||
|SD8|Card Output Data Window|tODW|0.5 x tCLK|—|ns|



1Data window in SDR104 mode is variable. 

**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

NXP Semiconductors 

77 

**Electrical Characteristics** 

## **4.9.3.4 HS200 mode timing** 

Figure 46 depicts the timing of HS200 mode, and Table 63 lists the HS200 timing characteristics. 

**==> picture [486 x 394] intentionally omitted <==**

**----- Start of picture text -----**<br>
SD1<br>SD2 SD3<br>SCK<br>SD4/SD5<br>8-bit output from uSDHC to eMMC<br>8-bit input from eMMC to uSDHC<br>SD8<br>Figure 46. HS200 mode timing<br>Table 63. HS200 interface timing specification<br>ID Parameter Symbols  Min Max Unit<br>Card Input Clock<br>SD1 Clock Frequency Period tCLK 5.0 — ns<br>SD2 Clock Low Time tCL 0.46 x tCLK 0.54 x tCLK ns<br>SD3 Clock High Time tCH 0.46 x tCLK 0.54 x tCLK ns<br>uSDHC Output/Card Inputs SD_CMD, SDx_DATAx in HS200 (Reference to CLK)<br>SD5 uSDHC Output Delay tOD –1.6 0.74 ns<br>uSDHC Input/Card Outputs SD_CMD, SDx_DATAx in HS200 (Reference to CLK) [1]<br>SD8 Card Output Data Window tODW 0.5 x tCLK — ns<br>1HS200 is for 8 bits while SDR104 is for 4 bits.<br>**----- End of picture text -----**<br>


## **4.9.3.5 Bus operation condition for 3.3 V and 1.8 V signaling** 

Signaling level of SD/eMMC4.3 and eMMC4.4/4.41 modes is 3.3 V. Signaling level of SDR104/SDR50 mode is 1.8 V. The DC parameters for the NVCC_SD1 supply are identical to those shown in Table 22, "Single voltage GPIO DC parameters," on page 37. 

## **4.9.4 Ethernet controller (ENET) AC electrical specifications** 

The following timing specs are defined at the chip I/O pin and must be translated appropriately to arrive at timing specs/constraints for the physical interface. 

**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

78 

NXP Semiconductors 

**Electrical Characteristics** 

## **4.9.4.1 ENET MII mode timing** 

This subsection describes MII receive, transmit, asynchronous inputs, and serial management signal timings. 

## **4.9.4.1.1 MII receive signal timing (ENET_RX_DATA3,2,1,0, ENET_RX_EN, ENET_RX_ER, and ENET_RX_CLK)** 

The receiver functions correctly up to an ENET_RX_CLK maximum frequency of 25 MHz + 1%. There is no minimum frequency requirement. Additionally, the processor clock frequency must exceed twice the ENET_RX_CLK frequency. 

Figure 47 shows MII receive signal timings. Table 64 describes the timing parameters (M1–M4) shown in the figure. 

**==> picture [474 x 147] intentionally omitted <==**

**----- Start of picture text -----**<br>
M3<br>ENET_RX_CLK (input)<br>M4<br>ENET_RX_DATA3,2,1,0<br>(inputs)<br>ENET_RX_EN<br>ENET_RX_ER<br>M1 M2<br>**----- End of picture text -----**<br>


## **Figure 47. MII receive signal timing diagram** 

## **Table 64. MII receive signal timing** 

|**ID**|**Characteristic1**|**Min.**|**Max.**|**Unit**|
|---|---|---|---|---|
|M1|ENET_RX_DATA3,2,1,0, ENET_RX_EN, ENET_RX_ER to<br>ENET_RX_CLK setup|5|—|ns|
|M2|ENET_RX_CLK to ENET_RX_DATA3,2,1,0, ENET_RX_EN,<br>ENET_RX_ER hold|5|—|ns|
|M3|ENET_RX_CLK pulse width high|35%|65%|ENET_RX_CLK period|
|M4|ENET_RX_CLK pulse width low|35%|65%|ENET_RX_CLK period|



1 ENET_RX_EN, ENET_RX_CLK, and ENET0_RXD0 have the same timing in 10 Mbps 7-wire interface mode. 

## **4.9.4.1.2 MII transmit signal timing (ENET_TX_DATA3,2,1,0, ENET_TX_EN, ENET_TX_ER, and ENET_TX_CLK)** 

The transmitter functions correctly up to an ENET_TX_CLK maximum frequency of 25 MHz + 1%. There is no minimum frequency requirement. Additionally, the processor clock frequency must exceed twice the ENET_TX_CLK frequency. 

**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

NXP Semiconductors 

79 

## **Electrical Characteristics** 

Figure 48 shows MII transmit signal timings. Table 65 describes the timing parameters (M5–M8) shown in the figure. 

**==> picture [473 x 146] intentionally omitted <==**

**----- Start of picture text -----**<br>
M7<br>ENET_TX_CLK (input)<br>M5<br>M8<br>ENET_TX_DATA3,2,1,0<br>(outputs)<br>ENET_TX_EN<br>ENET_TX_ER<br>M6<br>**----- End of picture text -----**<br>


## **Figure 48. MII transmit signal timing diagram** 

## **Table 65. MII transmit signal timing** 

|**ID**|**Characteristic1**|**Min.**|**Max.**|**Unit**|
|---|---|---|---|---|
|M5|ENET_TX_CLK to ENET_TX_DATA3,2,1,0, ENET_TX_EN,<br>ENET_TX_ER invalid|5|—|ns|
|M6|ENET_TX_CLK to ENET_TX_DATA3,2,1,0, ENET_TX_EN,<br>ENET_TX_ER valid|—|20|ns|
|M7|ENET_TX_CLK pulse width high|35%|65%|ENET_TX_CLK period|
|M8|ENET_TX_CLK pulse width low|35%|65%|ENET_TX_CLK period|



1 ENET_TX_EN, ENET_TX_CLK, and ENET0_TXD0 have the same timing in 10-Mbps 7-wire interface mode. 

## **4.9.4.1.3 MII asynchronous inputs signal timing (ENET_CRS and ENET_COL)** 

Figure 49 shows MII asynchronous input timings. Table 66 describes the timing parameter (M9) shown in the figure. 

ENET_CRS, ENET_COL 

M9 

## **Figure 49. MII asynchronous inputs timing diagram** 

## **Table 66. MII asynchronous inputs signal timing** 

|**ID**|**Characteristic**|**Min.**|**Max.**|**Unit**|
|---|---|---|---|---|
|M91|ENET_CRS to ENET_COL minimum pulse width|1.5|—|ENET_TX_CLK period|



1 ENET_COL has the same timing in 10-Mbit 7-wire interface mode. 

**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

80 

NXP Semiconductors 

**Electrical Characteristics** 

## **4.9.4.1.4 MII serial management channel timing (ENET_MDIO and ENET_MDC)** 

The MDC frequency is designed to be equal to or less than 2.5 MHz to be compatible with the IEEE 802.3 MII specification. However the ENET can function correctly with a maximum MDC frequency of 15 MHz. 

Figure 50 shows MII asynchronous input timings. Table 67 describes the timing parameters (M10–M15) shown in the figure. 

**==> picture [470 x 226] intentionally omitted <==**

**----- Start of picture text -----**<br>
M14<br>M15<br>ENET_MDC (output)<br>M10<br>ENET_MDIO (output)<br>M11<br>ENET_MDIO (input)<br>M12 M13<br>**----- End of picture text -----**<br>


**Figure 50. MII serial management channel timing diagram** 

**Table 67. MII serial management channel timing** 

|**ID**|**Characteristic**|**Min.**|**Max.**|**Unit**|
|---|---|---|---|---|
|M10|ENET_MDC falling edge to ENET_MDIO output invalid (min.<br>propagation delay)|0|—|ns|
|M11|ENET_MDC falling edge to ENET_MDIO output valid (max.<br>propagation delay)|—|5|ns|
|M12|ENET_MDIO (input) to ENET_MDC rising edge setup|18|—|ns|
|M13|ENET_MDIO (input) to ENET_MDC rising edge hold|0|—|ns|
|M14|ENET_MDC pulse width high|40%|60%|ENET_MDC period|
|M15|ENET_MDC pulse width low|40%|60%|ENET_MDC period|



## **4.9.4.2 RMII mode timing** 

In RMII mode, ENET_CLK is used as the REF_CLK, which is a 50 MHz ± 50 ppm continuous reference clock. ENET_RX_EN is used as the ENET_RX_EN in RMII. Other signals under RMII mode include ENET_TX_EN, ENET_TX_DATA[1:0], ENET_RX_DATA[1:0] and ENET_RX_ER. 

**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

NXP Semiconductors 

81 

## **Electrical Characteristics** 

Figure 51 shows RMII mode timings. Table 68 describes the timing parameters (M16–M21) shown in the figure. 

**==> picture [477 x 227] intentionally omitted <==**

**----- Start of picture text -----**<br>
M16<br>M17<br>ENET_CLK (input)<br>M18<br>ENET_TX_DATA (output)<br>ENET_TX_EN<br>M19<br>ENET_RX_EN (input)<br>ENET_RX_DATA[1:0]<br>ENET_RX_ER<br>M20 M21<br>**----- End of picture text -----**<br>


## **Figure 51. RMII mode signal timing diagram** 

## **Table 68. RMII signal timing** 

|**ID**|**Characteristic**|**Min.**|**Max.**|**Unit**|
|---|---|---|---|---|
|M16|ENET_CLK pulse width high|35%|65%|ENET_CLK period|
|M17|ENET_CLK pulse width low|35%|65%|ENET_CLK period|
|M18|ENET_CLK to ENET0_TXD[1:0], ENET_TX_DATA invalid|4|—|ns|
|M19|ENET_CLK to ENET0_TXD[1:0], ENET_TX_DATA valid|—|13|ns|
|M20|ENET_RX_DATAD[1:0], ENET_RX_EN(ENET_RX_EN), ENET_RX_ER<br>to ENET_CLK setup|2|—|ns|
|M21|ENET_CLK to ENET_RX_DATAD[1:0], ENET_RX_EN, ENET_RX_ER<br>hold|2|—|ns|



## **4.9.5 Flexible Controller Area Network (FLEXCAN) AC electrical specifications** 

Please refer to Section 4.3.2.1, General purpose I/O AC parameters. 

## **4.9.6 LPUART electrical specifications** 

Please refer to Section 4.3.2.1, General purpose I/O AC parameters. 

**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

82 

NXP Semiconductors 

**Electrical Characteristics** 

## **4.9.7 USB PHY parameters** 

This section describes the USB-OTG PHY parameters. 

The USB PHY meets the electrical compliance requirements defined in the Universal Serial Bus Revision 2.0 OTG with the following amendments. 

- USB ENGINEERING CHANGE NOTICE 

   - Title: 5V Short Circuit Withstand Requirement Change 

   - Applies to: Universal Serial Bus Specification, Revision 2.0 

- Errata for USB Revision 2.0 April 27, 2000 as of 12/7/2000 

- USB ENGINEERING CHANGE NOTICE 

   - Title: Pull-up/Pull-down resistors 

   - Applies to: Universal Serial Bus Specification, Revision 2.0 

- USB ENGINEERING CHANGE NOTICE 

   - Title: Suspend Current Limit Changes 

   - Applies to: Universal Serial Bus Specification, Revision 2.0 

- USB ENGINEERING CHANGE NOTICE 

   - Title: USB 2.0 Phase Locked SOFs 

   - Applies to: Universal Serial Bus Specification, Revision 2.0 

- On-The-Go and Embedded Host Supplement to the USB Revision 2.0 Specification — Revision 2.0 plus errata and ecn June 4, 2010 

- Battery Charging Specification (available from USB-IF) 

   - Revision 1.2, December 7, 2010 

   - Portable device only 

## **4.10 Timers** 

This section provide information on timers. 

## **4.10.1 Pulse Width Modulator (PWM) characteristics** 

This section describes the electrical information of the PWM. 

## **Table 69. PWM timing parameters** 

|**Parameter**|**Symbol**|**Min**|**Typ**|**Max**|**Unit**|
|---|---|---|---|---|---|
|PWM Clock Frequency|—|—|—|150|MHz|



## **4.10.2 Quad timer timing** 

Table 70 listed the timing parameters. 

**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

NXP Semiconductors 

83 

## **Electrical Characteristics** 

## **Table 70. Quad timer timing** 

|**Characteristic**|**Characteristic**|**Characteristic**|**Characteristic**|**Characteristic**|**Symbo**|**Symbo**|**Min1**|**Min1**|**Max**|**Max**|**Unit**|**Unit**|**Unit**|**See Figure**|**See Figure**|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Timer input period|||||TIN||2T + 6||—|—|ns||ns|||
|Timer input high/low period|||||TINHL||1T + 3||—|—|ns||ns|||
|Timer output period|||||TOUT||33||—|—|ns||ns|||
|Timer output high/low period|||||TOUTHL||16.7||—|—|ns||ns|||
|1T = clock cycle. For 60 MHz operation, T = 16.7 ns.||T = clock cycle. For 60 MHz operation, T = 16.7 ns.||||||||||||||
|1T = clock cycle. For 60 MHz operation, T = 16.7 ns.<br>Timer Inputs<br>Timer Outputs||T = clock cycle. For 60 MHz operation, T = 16.7 ns.<br>TIN||||||||TINHL||||||
|||||||||TINHL||TINHL||||||
|||||||||||||||||
|||||||||||||||||
||||T|||||||||||||
||||TIN|||||TINHL||||||||
||Timer Outputs|||||||yOUTHL||TOUTHL||||||
|||||||||||||||||
|||||||||||||||||
||||T|||||||||||||
||||TOUT|||||yOUTHL||TOUTHL||||||



**Figure 52. Quad timer timing** 

**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

84 

NXP Semiconductors 

**Boot mode configuration** 

## **5 Boot mode configuration** 

This section provides information on boot mode configuration pins allocation and boot devices interfaces allocation. 

## **5.1 Boot mode configuration pins** 

Table 71 provides boot options, functionality, fuse values, and associated pins. Several input pins are also sampled at reset and can be used to override fuse values, depending on the value of BT_FUSE_SEL fuse. The boot option pins are in effect when BT_FUSE_SEL fuse is ‘0’ (cleared, which is the case for an unblown fuse). For detailed boot mode options configured by the boot mode pins, see the i.MX RT1060 Fuse Map document and the System Boot chapter in _i.MX RT1060 Reference Manual (_ IMXRT1060RM _)_ . 

**Table 71. Fuses and associated pins used for boot** 

|**Pad**|**Default setting on reset**|**eFuse name**|**Details**|
|---|---|---|---|
|GPIO_AD_B0_04|100 K pull-down|BOOT_MODE0||
|GPIO_AD_B0_05|100 K pull-down|BOOT_MODE1||
|GPIO_B0_04|100 K pull-down|BT_CFG[0]|Boot Options, Pin value overrides<br>fuse settings for BT_FUSE_SEL =<br>‘0’. Signal Configuration as Fuse<br>Override Input at Power Up.<br>These are special I/O lines that<br>control the boot up configuration<br>during product development. In<br>production, the boot configuration<br>can be controlled by fuses.|
|GPIO_B0_05|100 K pull-down|BT_CFG[1]||
|GPIO_B0_06|100 K pull-down|BT_CFG[2]||
|GPIO_B0_07|100 K pull-down|BT_CFG[3]||
|GPIO_B0_08|100 K pull-down|BT_CFG[4]||
|GPIO_B0_09|100 K pull-down|BT_CFG[5]||
|GPIO_B0_10|100 K pull-down|BT_CFG[6]||
|GPIO_B0_11|100 K pull-down|BT_CFG[7]||
|GPIO_B0_12|100 K pull-down|BT_CFG[8]||
|GPIO_B0_13|100 K pull-down|BT_CFG[9]||
|GPIO_B0_14|100 K pull-down|BT_CFG[10]||
|GPIO_B0_15|100 K pull-down|BT_CFG[11]||



## **5.2 Boot device interface allocation** 

The following tables list the interfaces that can be used by the boot process in accordance with the specific boot mode configuration. The tables also describe the interface’s specific modes and IOMUXC allocation, which are configured during boot when appropriate. 

**Table 72. Boot trough NAND** 

|**PAD Name**|**IO Function**|**ALT**|**Comments**|
|---|---|---|---|
|GPIO_EMC_00|semc.DATA[0]|ALT 0|—|
|GPIO_EMC_01|semc.DATA[1]|ALT 0|—|
|GPIO_EMC_02|semc.DATA[2]|ALT 0|—|



**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

NXP Semiconductors 

85 

## **Boot mode configuration** 

## **Table 72. Boot trough NAND** 

||**Table 72. Boot trough NAND**|||
|---|---|---|---|
|GPIO_EMC_03|semc.DATA[3]|ALT 0|—|
|GPIO_EMC_04|semc.DATA[4]|ALT 0|—|
|GPIO_EMC_05|semc.DATA[5]|ALT 0|—|
|GPIO_EMC_06|semc.DATA[6]|ALT 0|—|
|GPIO_EMC_07|semc.DATA[7]|ALT 0|—|
|GPIO_EMC_30|semc.DATA[8]|ALT 0|—|
|GPIO_EMC_31|semc.DATA[9]|ALT 0|—|
|GPIO_EMC_32|semc.DATA[10]|ALT 0|—|
|GPIO_EMC_33|semc.DATA[11]|ALT 0|—|
|GPIO_EMC_34|semc.DATA[12]|ALT 0|—|
|GPIO_EMC_35|semc.DATA[13]|ALT 0|—|
|GPIO_EMC_36|semc.DATA[14]|ALT 0|—|
|GPIO_EMC_37|semc.DATA[15]|ALT 0|—|
|GPIO_EMC_18|semc.ADDR[9]|ALT 0|—|
|GPIO_EMC_19|semc.ADDR[11]|ALT 0|—|
|GPIO_EMC_20|semc.ADDR[12]|ALT 0|—|
|GPIO_EMC_22|semc.BA1|ALT 0|—|
|GPIO_EMC_41|semc.CSX[0]|ALT 0|—|



## **Table 73. Boot trough NOR** 

|**PAD Name**|**IO Function**|**ALT**|**Comments**|
|---|---|---|---|
|GPIO_EMC_00|semc.DATA[0]|ALT 0|—|
|GPIO_EMC_01|semc.DATA[1]|ALT 0|—|
|GPIO_EMC_02|semc.DATA[2]|ALT 0|—|
|GPIO_EMC_03|semc.DATA[3]|ALT 0|—|
|GPIO_EMC_04|semc.DATA[4]|ALT 0|—|
|GPIO_EMC_05|semc.DATA[5]|ALT 0|—|
|GPIO_EMC_06|semc.DATA[6]|ALT 0|—|
|GPIO_EMC_07|semc.DATA[7]|ALT 0|—|
|GPIO_EMC_30|semc.DATA[8]|ALT 0|—|
|GPIO_EMC_31|semc.DATA[9]|ALT 0|—|
|GPIO_EMC_32|semc.DATA[10]|ALT 0|—|
|GPIO_EMC_33|semc.DATA[11]|ALT 0|—|



**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

86 

NXP Semiconductors 

**Boot mode configuration** 

## **Table 73. Boot trough NOR** 

||**Table 73. Boot trough NOR**|||
|---|---|---|---|
|GPIO_EMC_34|semc.DATA[12]|ALT 0|—|
|GPIO_EMC_35|semc.DATA[13]|ALT 0|—|
|GPIO_EMC_36|semc.DATA[14]|ALT 0|—|
|GPIO_EMC_37|semc.DATA[15]|ALT 0|—|
|GPIO_EMC_09|semc.ADDR[0]|ALT 0|—|
|GPIO_EMC_10|semc.ADDR[1]|ALT 0|—|
|GPIO_EMC_11|semc.ADDR[2]|ALT 0|—|
|GPIO_EMC_12|semc.ADDR[3]|ALT 0|—|
|GPIO_EMC_13|semc.ADDR[4]|ALT 0|—|
|GPIO_EMC_14|semc.ADDR[5]|ALT 0|—|
|GPIO_EMC_15|semc.ADDR[6]|ALT 0|—|
|GPIO_EMC_16|semc.ADDR[7]|ALT 0|—|
|GPIO_EMC_19|semc.ADDR[11]|ALT 0|—|
|GPIO_EMC_20|semc.ADDR[12]|ALT 0|—|
|GPIO_EMC_21|semc.BA0|ALT 0|—|
|GPIO_EMC_22|semc.BA1|ALT 0|—|
|GPIO_EMC_41|semc.CSX[0]|ALT 0|—|



## **Table 74. Boot through FlexSPI** 

|**PAD Name**|**IO Function**|**Mux Mode**|**Comments**|
|---|---|---|---|
|GPIO_SD_B1_00|flexspi.B_DATA[3]|ALT 1|—|
|GPIO_SD_B1_01|flexspi.B_DATA[2]|ALT 1|—|
|GPIO_SD_B1_02|flexspi.B_DATA[1]|ALT 1|—|
|GPIO_SD_B1_03|flexspi.B_DATA[0]|ALT 1|—|
|GPIO_SD_B1_04|flexspi.B_SCLK|ALT 1|—|
|GPIO_SD_B0_05|flexspi.B_DQS|ALT 4|—|
|GPIO_SD_B0_04|flexspi.B_SS0_B|ALT 4|—|
|GPIO_SD_B0_01|flexspi.B_SS1_B|ALT 6|—|
|GPIO_SD_B1_05|flexspi.A_DQS|ALT 1|—|
|GPIO_SD_B1_06|flexspi.A_SS0_B|ALT 1|—|
|GPIO_SD_B0_00|flexspi.A_SS1_B|ALT 6|—|
|GPIO_SD_B1_07|flexspi.A_SCLK|ALT 1|—|
|GPIO_SD_B1_08|flexspi.A_DATA[0]|ALT 1|—|
|GPIO_SD_B1_09|flexspi.A_DATA[1]|ALT 1|—|



**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

NXP Semiconductors 

87 

## **Boot mode configuration** 

**Table 74. Boot through FlexSPI (continued)** 

|**PAD Name**|**IO Function**|**Mux Mode**|**Comments**|
|---|---|---|---|
|GPIO_SD_B1_10|flexspi.A_DATA[2]|ALT 1|—|
|GPIO_SD_B1_11|flexspi.A_DATA[3]|ALT 1|—|
|**Table 75. Boot through SD1**||||
|**PAD Name**|**IO Function**|**Mux Mode**|**Comments**|
|GPIO_SD_B0_00|usdhc1.CMD|ALT 0|—|
|GPIO_SD_B0_01|usdhc1.CLK|ALT 0|—|
|GPIO_SD_B0_02|usdhc1.DATA0|ALT 0|—|
|GPIO_SD_B0_03|usdhc1.DATA1|ALT 0|—|
|GPIO_SD_B0_04|usdhc1.DATA2|ALT 0|—|
|GPIO_SD_B0_05|usdhc1.DATA3|ALT 0|—|
|**Table 76. Boot through SD2**||||
|**PAD Name**|**IO Function**|**Mux Mode**|**Comments**|
|GPIO_SD_B1_00|usdhc2.DATA3|ALT 0|—|
|GPIO_SD_B1_01|usdhc2.DATA2|ALT 0|—|
|GPIO_SD_B1_02|usdhc2.DATA1|ALT 0|—|
|GPIO_SD_B1_03|usdhc2.DATA0|ALT 0|—|
|GPIO_SD_B1_04|usdhc2.CLK|ALT 0|—|
|GPIO_SD_B1_05|usdhc2.CMD|ALT 0|—|
|GPIO_SD_B1_06|usdhc2.RESET_B|ALT 0|—|
|GPIO_SD_B1_08|usdhc2.DATA4|ALT 0|—|
|GPIO_SD_B1_09|usdhc2.DATA5|ALT 0|—|
|GPIO_SD_B1_10|usdhc2.DATA6|ALT 0|—|
|GPIO_SD_B1_11|usdhc2.DATA7|ALT 0|—|



## **Table 77. Boot through SPI-1** 

|**PAD Name**|**IO Function**|**Mux Mode**|**Comments**|
|---|---|---|---|
|GPIO_SD_B0_00|lpspi1.SCK|ALT 4|—|
|GPIO_SD_B0_02|lpspi1.SDO|ALT 4|—|
|GPIO_SD_B0_03|lpspi1.SDI|ALT 4|—|
|GPIO_SD_B0_01|lpspi1.PCS0|ALT 4|—|



**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

88 

NXP Semiconductors 

**Boot mode configuration** 

## **Table 78. Boot through SPI-2** 

|**PAD Name**|**IO Function**|**Mux Mode**|**Comments**|
|---|---|---|---|
|GPIO_SD_B1_07|lpspi2.SCK|ALT 4|—|
|GPIO_SD_B1_08|lpspi2.SDO|ALT 4|—|
|GPIO_SD_B1_09|lpspi2.SDI|ALT 4|—|
|GPIO_SD_B1_06|lpspi2.PCS0|ALT 4|—|



## **Table 79. Boot through SPI-3** 

|**PAD Name**|**IO Function**|**Mux Mode**|**Comments**|
|---|---|---|---|
|GPIO_AD_B0_00|lpspi3.SCK|ALT 7|—|
|GPIO_AD_B0_01|lpspi3.SDO|ALT 7|—|
|GPIO_AD_B0_02|lpspi3.SDI|ALT 7|—|
|GPIO_SD_B0_03|lpspi3.PCS0|ALT 7|—|



## **Table 80. Boot through SPI-4** 

|**PAD Name**|**IO Function**|**Mux Mode**|**Comments**|
|---|---|---|---|
|GPIO_B0_03|lpspi4.SCK|ALT 3|—|
|GPIO_B0_02|lpspi4.SDO|ALT 3|—|
|GPIO_B0_01|lpspi4.SDI|ALT 3|—|
|GPIO_B0_00|lpspi4.PCS0|ALT 3|—|



## **Table 81. Boot through UART1** 

|**PAD Name**|**IO Function**|**Mux Mode**|**Comments**|
|---|---|---|---|
|GPIO_AD_B0_12|lpuart1.TX|ALT 2|—|
|GPIO_AD_B0_13|lpuart1.RX|ALT 2|—|



**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

NXP Semiconductors 

89 

**Package information and contact assignments** 

## **6 Package information and contact assignments** 

This section includes the contact assignment information and mechanical package drawing. 

## **6.1 10 x 10 mm package information** 

## **6.1.1 10 x 10 mm, 0.65 mm pitch, ball matrix** 

Figure 53 shows the top, bottom, and side views of the 10 x 10 mm MAPBGA package. 

**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

90 

NXP Semiconductors 

**Package information and contact assignments** 

**==> picture [385 x 410] intentionally omitted <==**

**==> picture [394 x 90] intentionally omitted <==**

**Figure 53. 10 x 10 mm BGA, case x package top, bottom, and side Views** 

**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

NXP Semiconductors 

91 

## **Package information and contact assignments** 

## **6.1.2 10 x 10 mm supplies contact assignments and functional contact assignments** 

Table 82 shows the device connection list for ground, sense, and reference contact signals. 

**Table 82. 10 x 10 mm supplies contact assignment** 

|**Supply Rail Name**|**Ball(s) Position(s)**|**Remark**|
|---|---|---|
|DCDC_IN|L1, L2|—|
|DCDC_IN_Q|K4|—|
|DCDC_GND|N1, N2|—|
|DCDC_LP|M1, M2|—|
|DCDC_PSWITCH|K3|—|
|DCDC_SENSE|J5|—|
|GPANAIO|N10|—|
|NGND_KEL0|K9|—|
|NVCC_EMC|E6, F5|—|
|NVCC_GPIO|E9, F10, J10|—|
|NVCC_PLL|P10|—|
|NVCC_SD0|J6|—|
|NVCC_SD1|K5|—|
|VDDA_ADC_3P3|N14|—|
|VDD_HIGH_CAP|P8|—|
|VDD_HIGH_IN|P12|—|
|VDD_SNVS_CAP|M10|—|
|VDD_SNVS_IN|M9|—|
|VDD_SOC_IN|F6, F7, F8, F9, G6, G9, H6, H9, J9|—|
|VDD_USB_CAP|K8|—|
|VSS|A1, A14, B5, B10, E2, E13, G7, G8, H7, H8, J7, J8, K2, K13, L9, N5, N8, P1, P14|—|



Table 83 shows an alpha-sorted list of functional contact assignments for the 10 x 10 mm package. 

**Table 83. 10 x 10 mm functional contact assignments** 

|**Ball Name**|**10 x**<br>**10**<br>**Ball**|**Power**<br>**Group**|**Ball**<br>**Type**|**Default Setting**|**Default Setting**|**Default Setting**|**Default Setting**|**Default setting on**<br>**Reset**|**Default setting on**<br>**Reset**|
|---|---|---|---|---|---|---|---|---|---|
|||||**Default**<br>**Mode**|**Default**<br>**Function**|**Input/**<br>**Output**|**Value**|**Input/**<br>**Output**|**Value**|
|CCM_CLK1_N|P13|—|—|—|CCM_CLK1_N|—|—|—|—|
|CCM_CLK1_P|N13|—|—|—|CCM_CLK1_P|—|—|—|—|



**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

92 

NXP Semiconductors 

**Package information and contact assignments** 

**Table 83. 10 x 10 mm functional contact assignments (continued)** 

|GPIO_AD_B0_00|M14|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO1.IO[0]|Input|Keeper|Input|Keeper|
|---|---|---|---|---|---|---|---|---|---|
|GPIO_AD_B0_01|H10|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO1.IO[1]|Input|Keeper|Input|Keeper|
|GPIO_AD_B0_02|M11|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO1.IO[2]|Input|Keeper|Input|Keeper|
|GPIO_AD_B0_03|G11|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO1.IO[3]|Input|Keeper|Input|Keeper|
|GPIO_AD_B0_04|F11|NVCC_GPIO|Digital<br>GPIO|ALT0|SRC.BOOT.MO<br>DE[0]|Input|100 K<br>PD|Input|100 K<br>PD|
|GPIO_AD_B0_05|G14|NVCC_GPIO|Digital<br>GPIO|ALT0|SRC.BOOT.MO<br>DE[1]|Input|100 K<br>PD|Input|100 K<br>PD|
|GPIO_AD_B0_06|E14|NVCC_GPIO|Digital<br>GPIO|ALT0|JTAG.MUX.TMS|Input|47 K PU|Input|47 K PU|
|GPIO_AD_B0_07|F12|NVCC_GPIO|Digital<br>GPIO|ALT0|JTAG.MUX.TCK|Input|47 K PU|Input|100 K<br>PD|
|GPIO_AD_B0_08|F13|NVCC_GPIO|Digital<br>GPIO|ALT0|JTAG.MUX.MOD|Input|100 K<br>PU|Input|100 K<br>PD|
|GPIO_AD_B0_09|F14|NVCC_GPIO|Digital<br>GPIO|ALT0|JTAG.MUX.TDI|Input|47 K PU|Input|47 K PU|
|GPIO_AD_B0_10|G13|NVCC_GPIO|Digital<br>GPIO|ALT0|JTAG.MUX.TDO|Output|Keeper|Output|Keeper|
|GPIO_AD_B0_11|G10|NVCC_GPIO|Digital<br>GPIO|ALT0|JTAG.MUX.TRS<br>TB|Input|47 K PU|Input|47 K PU|
|GPIO_AD_B0_12|K14|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO1.IO[12]|Input|Keeper|Input|Keeper|
|GPIO_AD_B0_13|L14|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO1.IO[13]|Input|Keeper|Input|Keeper|
|GPIO_AD_B0_14|H14|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO1.IO[14]|Input|Keeper|Input|Keeper|
|GPIO_AD_B0_15|L10|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO1.IO[15]|Input|Keeper|Input|Keeper|
|GPIO_AD_B1_00|J11|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO1.IO[16]|Input|Keeper|Input|Keeper|
|GPIO_AD_B1_01|K11|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO1.IO[17]|Input|Keeper|Input|Keeper|
|GPIO_AD_B1_02|L11|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO1.IO[18]|Input|Keeper|Input|Keeper|
|GPIO_AD_B1_03|M12|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO1.IO[19]|Input|Keeper|Input|Keeper|
|GPIO_AD_B1_04|L12|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO1.IO[20]|Input|Keeper|Input|Keeper|



**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

NXP Semiconductors 

93 

**Package information and contact assignments** 

**Table 83. 10 x 10 mm functional contact assignments (continued)** 

|GPIO_AD_B1_05|K12|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO1.IO[21]|Input|Keeper|Input|Keeper|
|---|---|---|---|---|---|---|---|---|---|
|GPIO_AD_B1_06|J12|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO1.IO[22]|Input|Keeper|Input|Keeper|
|GPIO_AD_B1_07|K10|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO1.IO[23]|Input|Keeper|Input|Keeper|
|GPIO_AD_B1_08|H13|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO1.IO[24]|Input|Keeper|Input|Keeper|
|GPIO_AD_B1_09|M13|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO1.IO[25]|Input|Keeper|Input|Keeper|
|GPIO_AD_B1_10|L13|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO1.IO[26]|Input|Keeper|Input|Keeper|
|GPIO_AD_B1_11|J13|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO1.IO[27]|Input|Keeper|Input|Keeper|
|GPIO_AD_B1_12|H12|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO1.IO[28]|Input|Keeper|Input|Keeper|
|GPIO_AD_B1_13|H11|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO1.IO[29]|Input|Keeper|Input|Keeper|
|GPIO_AD_B1_14|G12|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO1.IO[30]|Input|Keeper|Input|Keeper|
|GPIO_AD_B1_15|J14|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO1.IO[31]|Input|Keeper|Input|Keeper|
|GPIO_B0_00|D7|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO2.IO[0]|Input|Keeper|Input|Keeper|
|GPIO_B0_01|E7|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO2.IO[1]|Input|Keeper|Input|Keeper|
|GPIO_B0_02|E8|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO2.IO[2]|Input|Keeper|Input|Keeper|
|GPIO_B0_03|D8|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO2.IO[3]|Input|Keeper|Input|Keeper|
|GPIO_B0_04|C8|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO2.IO[4]|Input|Keeper|Input|100 K<br>PD|
|GPIO_B0_05|B8|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO2.IO[5]|Input|Keeper|Input|100 K<br>PD|
|GPIO_B0_06|A8|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO2.IO[6]|Input|Keeper|Input|100 K<br>PD|
|GPIO_B0_07|A9|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO2.IO[7]|Input|Keeper|Input|100 K<br>PD|
|GPIO_B0_08|B9|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO2.IO[8]|Input|Keeper|Input|100 K<br>PD|
|GPIO_B0_09|C9|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO2.IO[9]|Input|Keeper|Input|100 K<br>PD|



**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

94 

NXP Semiconductors 

**Package information and contact assignments** 

**Table 83. 10 x 10 mm functional contact assignments (continued)** 

|GPIO_B0_10|D9|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO2.IO[10]|Input|Keeper|Input|100 K<br>PD|
|---|---|---|---|---|---|---|---|---|---|
|GPIO_B0_11|A10|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO2.IO[11]|Input|Keeper|Input|100 K<br>PD|
|GPIO_B0_12|C10|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO2.IO[12]|Input|Keeper|Input|100 K<br>PD|
|GPIO_B0_13|D10|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO2.IO[13]|Input|Keeper|Input|100 K<br>PD|
|GPIO_B0_14|E10|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO2.IO[14]|Input|Keeper|Input|100 K<br>PD|
|GPIO_B0_15|E11|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO2.IO[15]|Input|Keeper|Input|100 K<br>PD|
|GPIO_B1_00|A11|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO2.IO[16]|Input|Keeper|Input|Keeper|
|GPIO_B1_01|B11|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO2.IO[17]|Input|Keeper|Input|Keeper|
|GPIO_B1_02|C11|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO2.IO[18]|Input|Keeper|Input|Keeper|
|GPIO_B1_03|D11|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO2.IO[19]|Input|Keeper|Input|Keeper|
|GPIO_B1_04|E12|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO2.IO[20]|Input|Keeper|Input|Keeper|
|GPIO_B1_05|D12|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO2.IO[21]|Input|Keeper|Input|Keeper|
|GPIO_B1_06|C12|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO2.IO[22]|Input|Keeper|Input|Keeper|
|GPIO_B1_07|B12|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO2.IO[23]|Input|Keeper|Input|Keeper|
|GPIO_B1_08|A12|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO2.IO[24]|Input|Keeper|Input|Keeper|
|GPIO_B1_09|A13|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO2.IO[25]|Input|Keeper|Input|Keeper|
|GPIO_B1_10|B13|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO2.IO[26]|Input|Keeper|Input|Keeper|
|GPIO_B1_11|C13|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO2.IO[27]|Input|Keeper|Input|Keeper|
|GPIO_B1_12|D13|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO2.IO[28]|Input|Keeper|Input|Keeper|
|GPIO_B1_13|D14|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO2.IO[29]|Input|Keeper|Input|Keeper|
|GPIO_B1_14|C14|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO2.IO[30]|Input|Keeper|Input|Keeper|



**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

NXP Semiconductors 

95 

**Package information and contact assignments** 

**Table 83. 10 x 10 mm functional contact assignments (continued)** 

|GPIO_B1_15|B14|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO2.IO[31]|Input|Keeper|Input|Keeper|
|---|---|---|---|---|---|---|---|---|---|
|GPIO_EMC_00|E3|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO4.IO[0]|Input|Keeper|Input|Keeper|
|GPIO_EMC_01|F3|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO4.IO[1]|Input|Keeper|Input|Keeper|
|GPIO_EMC_02|F4|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO4.IO[2]|Input|Keeper|Input|Keeper|
|GPIO_EMC_03|G4|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO4.IO[3]|Input|Keeper|Output1|Keeper|
|GPIO_EMC_04|F2|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO4.IO[4]|Input|Keeper|Input|Keeper|
|GPIO_EMC_05|G5|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO4.IO[5]|Input|Keeper|Input|Keeper|
|GPIO_EMC_06|H5|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO4.IO[6]|Input|Keeper|Input|Keeper|
|GPIO_EMC_07|H4|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO4.IO[7]|Input|Keeper|Input|Keeper|
|GPIO_EMC_08|H3|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO4.IO[8]|Input|Keeper|Input|Keeper|
|GPIO_EMC_09|C2|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO4.IO[9]|Input|Keeper|Input|Keeper|
|GPIO_EMC_10|G1|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO4.IO[10]|Input|Keeper|Input|Keeper|
|GPIO_EMC_11|G3|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO4.IO[11]|Input|Keeper|Input|Keeper|
|GPIO_EMC_12|H1|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO4.IO[12]|Input|Keeper|Input|Keeper|
|GPIO_EMC_13|A6|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO4.IO[13]|Input|Keeper|Input|Keeper|
|GPIO_EMC_14|B6|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO4.IO[14]|Input|Keeper|Input|Keeper|
|GPIO_EMC_15|B1|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO4.IO[15]|Input|Keeper|Input|Keeper|
|GPIO_EMC_16|A5|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO4.IO[16]|Input|Keeper|Input|Keeper|
|GPIO_EMC_17|A4|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO4.IO[17]|Input|Keeper|Input|Keeper|
|GPIO_EMC_18|B2|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO4.IO[18]|Input|Keeper|Input|Keeper|
|GPIO_EMC_19|B4|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO4.IO[19]|Input|Keeper|Input|Keeper|



**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

96 

NXP Semiconductors 

**Package information and contact assignments** 

**Table 83. 10 x 10 mm functional contact assignments (continued)** 

|GPIO_EMC_20|A3|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO4.IO[20]|Input|Keeper|Input|Keeper|
|---|---|---|---|---|---|---|---|---|---|
|GPIO_EMC_21|C1|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO4.IO[21]|Input|Keeper|Input|Keeper|
|GPIO_EMC_22|F1|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO4.IO[22]|Input|Keeper|Input|Keeper|
|GPIO_EMC_23|G2|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO4.IO[23]|Input|Keeper|Input|Keeper|
|GPIO_EMC_24|D3|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO4.IO[24]|Input|Keeper|Input|Keeper|
|GPIO_EMC_25|D2|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO4.IO[25]|Input|Keeper|Input|Keeper|
|GPIO_EMC_26|B3|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO4.IO[26]|Input|Keeper|Input|Keeper|
|GPIO_EMC_27|A2|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO4.IO[27]|Input|100 K<br>PD|Input|100 K<br>PD|
|GPIO_EMC_28|D1|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO4.IO[28]|Input|Keeper|Input|Keeper|
|GPIO_EMC_29|E1|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO4.IO[29]|Input|Keeper|Input|Keeper|
|GPIO_EMC_30|C6|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO4.IO[30]|Input|Keeper|Input|Keeper|
|GPIO_EMC_31|C5|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO4.IO[31]|Input|Keeper|Input|Keeper|
|GPIO_EMC_32|D5|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO3.IO[18]|Input|Keeper|Input|Keeper|
|GPIO_EMC_33|C4|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO3.IO[19]|Input|Keeper|Input|Keeper|
|GPIO_EMC_34|D4|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO3.IO[20]|Input|Keeper|Input|Keeper|
|GPIO_EMC_35|E5|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO3.IO[21]|Input|Keeper|Input|Keeper|
|GPIO_EMC_36|C3|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO3.IO[22]|Input|Keeper|Input|Keeper|
|GPIO_EMC_37|E4|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO3.IO[23]|Input|Keeper|Input|Keeper|
|GPIO_EMC_38|D6|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO3.IO[24]|Input|Keeper|Input|Keeper|
|GPIO_EMC_39|B7|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO3.IO[25]|Input|Keeper|Input|Keeper|
|GPIO_EMC_40|A7|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO3.IO[26]|Input|Keeper|Input|Keeper|



**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

NXP Semiconductors 

97 

**Package information and contact assignments** 

**Table 83. 10 x 10 mm functional contact assignments (continued)** 

|GPIO_EMC_41|C7|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO3.IO[27]|Input|Keeper|Input|Keeper|
|---|---|---|---|---|---|---|---|---|---|
|GPIO_SD_B0_00|J4|NVCC_SD0|Digital<br>GPIO|ALT5|GPIO3.IO[12]|Input|Keeper|Input|Keeper|
|GPIO_SD_B0_01|J3|NVCC_SD0|Digital<br>GPIO|ALT5|GPIO3.IO[13]|Input|Keeper|Input|Keeper|
|GPIO_SD_B0_02|J1|NVCC_SD0|Digital<br>GPIO|ALT5|GPIO3.IO[14]|Input|Keeper|Input|Keeper|
|GPIO_SD_B0_03|K1|NVCC_SD0|Digital<br>GPIO|ALT5|GPIO3.IO[15]|Input|Keeper|Input|Keeper|
|GPIO_SD_B0_04|H2|NVCC_SD0|Digital<br>GPIO|ALT5|GPIO3.IO[16]|Input|Keeper|Input|Keeper|
|GPIO_SD_B0_05|J2|NVCC_SD0|Digital<br>GPIO|ALT5|GPIO3.IO[17]|Input|Keeper|Input|Keeper|
|GPIO_SD_B1_00|L5|NVCC_SD1|Digital<br>GPIO|ALT5|GPIO3.IO[0]|Input|Keeper|Input|Keeper|
|GPIO_SD_B1_01|M5|NVCC_SD1|Digital<br>GPIO|ALT5|GPIO3.IO[1]|Input|Keeper|Input|Keeper|
|GPIO_SD_B1_02|M3|NVCC_SD1|Digital<br>GPIO|ALT5|GPIO3.IO[2]|Input|Keeper|Input|Keeper|
|GPIO_SD_B1_03|M4|NVCC_SD1|Digital<br>GPIO|ALT5|GPIO3.IO[3]|Input|Keeper|Input|Keeper|
|GPIO_SD_B1_04|P2|NVCC_SD1|Digital<br>GPIO|ALT5|GPIO3.IO[4]|Input|Keeper|Input|Keeper|
|GPIO_SD_B1_05|N3|NVCC_SD1|Digital<br>GPIO|ALT5|GPIO3.IO[5]|Input|Keeper|Input|Keeper|
|GPIO_SD_B1_06|L3|NVCC_SD1|Digital<br>GPIO|ALT5|GPIO3.IO[6]|Input|Keeper|Input|Keeper|
|GPIO_SD_B1_07|L4|NVCC_SD1|Digital<br>GPIO|ALT5|GPIO3.IO[7]|Input|Keeper|Input|Keeper|
|GPIO_SD_B1_08|P3|NVCC_SD1|Digital<br>GPIO|ALT5|GPIO3.IO[8]|Input|Keeper|Input|Keeper|
|GPIO_SD_B1_09|N4|NVCC_SD1|Digital<br>GPIO|ALT5|GPIO3.IO[9]|Input|Keeper|Input|Keeper|
|GPIO_SD_B1_10|P4|NVCC_SD1|Digital<br>GPIO|ALT5|GPIO3.IO[01]|Input|Keeper|Input|Keeper|
|GPIO_SD_B1_11|P5|NVCC_SD1|Digital<br>GPIO|ALT5|GPIO3.IO[11]|Input|Keeper|Input|Keeper|
|ONOFF|M6|VDD_SNVS_I<br>N|Digital<br>GPIO|ALT0|ONOFF|Input|100 K<br>PU|Input|100 K<br>PU|
|PMIC_ON_REQ|K7|VDD_SNVS_I<br>N|Digital<br>GPIO|ALT0|SNVS_LP.PMIC<br>_ON_REQ|Output|100 K<br>PU|Output|100 K<br>PU|



**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

98 

NXP Semiconductors 

**Package information and contact assignments** 

**Table 83. 10 x 10 mm functional contact assignments (continued)** 

|PMIC_STBY_REQ|L7|VDD_SNVS_I<br>N|Digital<br>GPIO|ALT0|CCM.PMIC_VST<br>BY_REQ|Output|100 K<br>PU<br>(PKE<br>disabled<br>)|Output|100 K<br>PU<br>(PKE<br>disabled<br>)|
|---|---|---|---|---|---|---|---|---|---|
|POR_B|M7|VDD_SNVS_I<br>N|Digital<br>GPIO|ALT0|SRC.POR_B|Input|100 K<br>PU|Input|100 K<br>PU|
|RTC_XTALI|N9|—|—|—|—|—|—|—|—|
|RTC_XTALO|P9|—|—|—|—|—|—|—|—|
|TEST_MODE|K6|VDD_SNVS_I<br>N|Digital<br>GPIO|ALT0|TCU.TEST_MO<br>DE|Input|100 K<br>PU|Input|100 K<br>PU|
|USB_OTG1_CHD<br>_B|N12|—|—|—|—|—|—|—|—|
|USB_OTG1_DN|M8|—|—|—|—|—|—|—|—|
|USB_OTG1_DP|L8|—|—|—|—|—|—|—|—|
|USB_OTG1_VBU<br>S|N6|—|—|—|—|—|—|—|—|
|USB_OTG2_DN|N7|—|—|—|—|—|—|—|—|
|USB_OTG2_DP|P7|—|—|—|—|—|—|—|—|
|USB_OTG2_VBU<br>S|P6|—|—|—|—|—|—|—|—|
|XTALI|P11|—|—|—|—|—|—|—|—|
|XTALO|N11|—|—|—|—|—|—|—|—|
|WAKEUP|L6|VDD_SNVS_I<br>N|Digital<br>GPIO|ALT5|GPIO5.IO[0]|Input|100 K<br>PU|Input|100 K<br>PU|



1 This pin output is in a high level until the system reset is complete. 

**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

NXP Semiconductors 

99 

**Package information and contact assignments** 

## **6.1.3 10 x 10 mm, 0.65 mm pitch, ball map** 

## Table 84 shows the 10 x 10 mm, 0.65 mm pitch ball map for the i.MX RT1060. 

**Table 84. 10x10 mm, 0.65 mm pitch, ball map** 

||**1**|**2**|**3**|**4**|**5**|**6**|**7**|**8**|**9**|**10**|**11**|**12**|**13**|**14**||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**A**|VSS|GPIO_EMC_27|GPIO_EMC_20|GPIO_EMC_17|GPIO_EMC_16|GPIO_EMC_13|GPIO_EMC_40|GPIO_B0_06|GPIO_B0_07|GPIO_B0_11|GPIO_B1_00|GPIO_B1_08|GPIO_B1_09|VSS|**A**|
|**B**|GPIO_EMC_15|GPIO_EMC_18|GPIO_EMC_26|GPIO_EMC_19|VSS|GPIO_EMC_14|GPIO_EMC_39|GPIO_B0_05|GPIO_B0_08|VSS|GPIO_B1_01|GPIO_B1_07|GPIO_B1_10|GPIO_B1_15|**B**|
|**C**|GPIO_EMC_21|GPIO_EMC_09|GPIO_EMC_36|GPIO_EMC_33|GPIO_EMC_31|GPIO_EMC_30|GPIO_EMC_41|GPIO_B0_04|GPIO_B0_09|GPIO_B0_12|GPIO_B1_02|GPIO_B1_06|GPIO_B1_11|GPIO_B1_14|**C**|
|**D**|GPIO_EMC_28|GPIO_EMC_25|GPIO_EMC_24|GPIO_EMC_34|GPIO_EMC_32|GPIO_EMC_38|GPIO_B0_00|GPIO_B0_03|GPIO_B0_10|GPIO_B0_13|GPIO_B1_03|GPIO_B1_05|GPIO_B1_12|GPIO_B1_13|**D**|
|**E**|GPIO_EMC_29|VSS|GPIO_EMC_00|GPIO_EMC_37|GPIO_EMC_35|NVCC_EMC|GPIO_B0_01|GPIO_B0_02|NVCC_GPIO|GPIO_B0_14|GPIO_B0_15|GPIO_B1_04|VSS|GPIO_AD_B0_06|**E**|
|**F**|GPIO_EMC_22|GPIO_EMC_04|GPIO_EMC_01|GPIO_EMC_02|NVCC_EMC|VDD_SOC_IN|VDD_SOC_IN|VDD_SOC_IN|VDD_SOC_IN|NVCC_GPIO|GPIO_AD_B0_04|GPIO_AD_B0_07|GPIO_AD_B0_08|GPIO_AD_B0_09|**F**|
|**G**|GPIO_EMC_10|GPIO_EMC_23|GPIO_EMC_11|GPIO_EMC_03|GPIO_EMC_05|VDD_SOC_IN|VSS|VSS|VDD_SOC_IN|GPIO_AD_B0_11|GPIO_AD_B0_03|GPIO_AD_B1_14|GPIO_AD_B0_10|GPIO_AD_B0_05|**G**|



**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

100 

NXP Semiconductors 

**Package information and contact assignments** 

**Table 84. 10x10 mm, 0.65 mm pitch, ball map (continued)** 

|**H**|GPIO_EMC_12|GPIO_SD_B0_04|GPIO_EMC_08|GPIO_EMC_07|GPIO_EMC_06|VDD_SOC_IN|VSS|VSS|VDD_SOC_IN|GPIO_AD_B0_01|GPIO_AD_B1_13|GPIO_AD_B1_12|GPIO_AD_B1_08|GPIO_AD_B0_14|**H**|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**J**|GPIO_SD_B0_02|GPIO_SD_B0_05|GPIO_SD_B0_01|GPIO_SD_B0_00|DCDC_SENSE|NVCC_SD0|VSS|VSS|VDD_SOC_IN|NVCC_GPIO|GPIO_AD_B1_00|GPIO_AD_B1_06|GPIO_AD_B1_11|GPIO_AD_B1_15|**J**|
|**K**|GPIO_SD_B0_03|VSS|DCDC_PSWITCH|DCDC__IN_Q|NVCC_SD1|TEST_MODE|PMIC_ON_REQ|VDD_USB_CAP|NGND_KEL0|GPIO_AD_B1_07|GPIO_AD_B1_01|GPIO_AD_B1_05|VSS|GPIO_AD_B0_12|**K**|
|**L**|DCDC_IN|DCDC_IN|GPIO_SD_B1_06|GPIO_SD_B1_07|GPIO_SD_B1_00|WAKEUP|PMIC_STBY_REQ|USB_OTG1_DP|VSS|GPIO_AD_B0_15|GPIO_AD_B1_02|GPIO_AD_B1_04|GPIO_AD_B1_10|GPIO_AD_B0_13|**L**|
|**M**|DCDC_LP|DCDC_LP|GPIO_SD_B1_02|GPIO_SD_B1_03|GPIO_SD_B1_01|ONOFF|POR_B|USB_OTG1_DN|VDD_SNVS_IN|VDD_SNVS_CAP|GPIO_AD_B0_02|GPIO_AD_B1_03|GPIO_AD_B1_09|GPIO_AD_B0_00|**M**|
|**N**|DCDC_GND|DCDC_GND|GPIO_SD_B1_05|GPIO_SD_B1_09|VSS|USB_OTG1_VBUS|USB_OTG2_DN|VSS|RTC_XTALI|GPANAIO|XTALO|USB_OTG1_CHD_B|CCM_CLK1_P|VDDA_ADC_3P3|**N**|
|**P**|VSS|GPIO_SD_B1_04|GPIO_SD_B1_08|GPIO_SD_B1_10|GPIO_SD_B1_11|USB_OTG2_VBUS|USB_OTG2_DP|VDD_HIGH_CAP|RTC_XTALO|NVCC_PLL|XTALI|VDD_HIGH_IN|CCM_CLK1_N|VSS|**P**|
||**1**|**2**|**3**|**4**|**5**|**6**|**7**|**8**|**9**|**10**|**11**|**12**|**13**|**14**||



**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

NXP Semiconductors 

101 

**Package information and contact assignments** 

## **6.2 12 x 12 mm package information** 

## **6.2.1 12 x 12 mm, 0.8 mm pitch, ball matrix** 

Figure 54 shows the top, bottom, and side views of the 12 x 12 mm MAPBGA package. 

**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

102 

NXP Semiconductors 

**Package information and contact assignments** 

**==> picture [201 x 225] intentionally omitted <==**

**==> picture [235 x 225] intentionally omitted <==**

**==> picture [105 x 345] intentionally omitted <==**

**==> picture [395 x 36] intentionally omitted <==**

**Figure 54. 12 x 12 mm BGA, case x package top, bottom, and side Views** 

**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

NXP Semiconductors 

103 

## **Package information and contact assignments** 

## **6.2.2 12 x 12 mm supplies contact assignments and functional contact assignments** 

Table 85 shows the device connection list for ground, sense, and reference contact signals. 

**Table 85. 12 x 12 mm supplies contact assignment** 

|**Supply Rail Name**|**Ball(s) Position(s)**|**Remark**|
|---|---|---|
|DCDC_IN|L1, L2|—|
|DCDC_IN_Q|K4|—|
|DCDC_GND|N1, N2|—|
|DCDC_LP|M1, M2|—|
|DCDC_PSWITCH|K3|—|
|DCDC_SENSE|J5|—|
|GPANAIO|N10|—|
|NGND_KEL0|K9|—|
|NVCC_EMC|E6, F5|—|
|NVCC_GPIO|E9, F10, J10|—|
|NVCC_PLL|P10|—|
|NVCC_SD0|J6|—|
|NVCC_SD1|K5|—|
|VDDA_ADC_3P3|N14|—|
|VDD_HIGH_CAP|P8|—|
|VDD_HIGH_IN|P12|—|
|VDD_SNVS_CAP|M10|—|
|VDD_SNVS_IN|M9|—|
|VDD_SOC_IN|F6, F7, F8, F9, G6, G9, H6, H9, J9|—|
|VDD_USB_CAP|K8|—|
|VSS|A1, A14, B5, B10, E2, E13, G7, G8, H7, H8, J7, J8, K2, K13, L9, N5, N8, P1, P14|—|



Table 86 shows an alpha-sorted list of functional contact assignments for the 12 x 12 mm package. This pin output is in a high level until the system reset is complete. 

**Table 86. 12 x 12 mm functional contact assignments** 

|**Ball Name**|**12 x**<br>**12**<br>**Ball**|**Power**<br>**Group**|**Ball**<br>**Type**|**Default Setting**|**Default Setting**|**Default Setting**|**Default Setting**|**Default setting on**<br>**Reset**|**Default setting on**<br>**Reset**|
|---|---|---|---|---|---|---|---|---|---|
|||||**Default**<br>**Mode**|**Default**<br>**Function**|**Input/**<br>**Output**|**Value**|**Input/**<br>**Output**|**Value**|
|CCM_CLK1_N|P13|—|—|—|CCM_CLK1_N|—|—|—|—|
|CCM_CLK1_P|N13|—|—|—|CCM_CLK1_P|—|—|—|—|



**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

104 

NXP Semiconductors 

**Package information and contact assignments** 

**Table 86. 12 x 12 mm functional contact assignments (continued)** 

|GPIO_AD_B0_00|M14|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO1.IO[0]|Input|Keeper|Input|Keeper|
|---|---|---|---|---|---|---|---|---|---|
|GPIO_AD_B0_01|H10|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO1.IO[1]|Input|Keeper|Input|Keeper|
|GPIO_AD_B0_02|M11|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO1.IO[2]|Input|Keeper|Input|Keeper|
|GPIO_AD_B0_03|G11|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO1.IO[3]|Input|Keeper|Input|Keeper|
|GPIO_AD_B0_04|F11|NVCC_GPIO|Digital<br>GPIO|ALT0|SRC.BOOT.MOD<br>E[0]|Input|100 K PD|Input|100 K PD|
|GPIO_AD_B0_05|G14|NVCC_GPIO|Digital<br>GPIO|ALT0|SRC.BOOT.MOD<br>E[1]|Input|100 K PD|Input|100 K PD|
|GPIO_AD_B0_06|E14|NVCC_GPIO|Digital<br>GPIO|ALT0|JTAG.MUX.TMS|Input|47 K PU|Input|47 K PU|
|GPIO_AD_B0_07|F12|NVCC_GPIO|Digital<br>GPIO|ALT0|JTAG.MUX.TCK|Input|47 K PU|Input|100 K PD|
|GPIO_AD_B0_08|F13|NVCC_GPIO|Digital<br>GPIO|ALT0|JTAG.MUX.MOD|Input|100 K PU|Input|100 K PD|
|GPIO_AD_B0_09|F14|NVCC_GPIO|Digital<br>GPIO|ALT0|JTAG.MUX.TDI|Input|47 K PU|Input|47 K PU|
|GPIO_AD_B0_10|G13|NVCC_GPIO|Digital<br>GPIO|ALT0|JTAG.MUX.TDO|Output|Keeper|Output|Keeper|
|GPIO_AD_B0_11|G10|NVCC_GPIO|Digital<br>GPIO|ALT0|JTAG.MUX.TRST<br>B|Input|47 K PU|Input|47 K PU|
|GPIO_AD_B0_12|K14|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO1.IO[12]|Input|Keeper|Input|Keeper|
|GPIO_AD_B0_13|L14|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO1.IO[13]|Input|Keeper|Input|Keeper|
|GPIO_AD_B0_14|H14|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO1.IO[14]|Input|Keeper|Input|Keeper|
|GPIO_AD_B0_15|L10|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO1.IO[15]|Input|Keeper|Input|Keeper|
|GPIO_AD_B1_00|J11|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO1.IO[16]|Input|Keeper|Input|Keeper|
|GPIO_AD_B1_01|K11|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO1.IO[17]|Input|Keeper|Input|Keeper|
|GPIO_AD_B1_02|L11|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO1.IO[18]|Input|Keeper|Input|Keeper|
|GPIO_AD_B1_03|M12|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO1.IO[19]|Input|Keeper|Input|Keeper|
|GPIO_AD_B1_04|L12|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO1.IO[20]|Input|Keeper|Input|Keeper|



**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

NXP Semiconductors 

105 

**Package information and contact assignments** 

**Table 86. 12 x 12 mm functional contact assignments (continued)** 

|GPIO_AD_B1_05|K12|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO1.IO[21]|Input|Keeper|Input|Keeper|
|---|---|---|---|---|---|---|---|---|---|
|GPIO_AD_B1_06|J12|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO1.IO[22]|Input|Keeper|Input|Keeper|
|GPIO_AD_B1_07|K10|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO1.IO[23]|Input|Keeper|Input|Keeper|
|GPIO_AD_B1_08|H13|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO1.IO[24]|Input|Keeper|Input|Keeper|
|GPIO_AD_B1_09|M13|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO1.IO[25]|Input|Keeper|Input|Keeper|
|GPIO_AD_B1_10|L13|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO1.IO[26]|Input|Keeper|Input|Keeper|
|GPIO_AD_B1_11|J13|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO1.IO[27]|Input|Keeper|Input|Keeper|
|GPIO_AD_B1_12|H12|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO1.IO[28]|Input|Keeper|Input|Keeper|
|GPIO_AD_B1_13|H11|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO1.IO[29]|Input|Keeper|Input|Keeper|
|GPIO_AD_B1_14|G12|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO1.IO[30]|Input|Keeper|Input|Keeper|
|GPIO_AD_B1_15|J14|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO1.IO[31]|Input|Keeper|Input|Keeper|
|GPIO_B0_00|D7|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO2.IO[0]|Input|Keeper|Input|Keeper|
|GPIO_B0_01|E7|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO2.IO[1]|Input|Keeper|Input|Keeper|
|GPIO_B0_02|E8|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO2.IO[2]|Input|Keeper|Input|Keeper|
|GPIO_B0_03|D8|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO2.IO[3]|Input|Keeper|Input|Keeper|
|GPIO_B0_04|C8|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO2.IO[4]|Input|Keeper|Input|100 K PD|
|GPIO_B0_05|B8|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO2.IO[5]|Input|Keeper|Input|100 K PD|
|GPIO_B0_06|A8|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO2.IO[6]|Input|Keeper|Input|100 K PD|
|GPIO_B0_07|A9|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO2.IO[7]|Input|Keeper|Input|100 K PD|
|GPIO_B0_08|B9|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO2.IO[8]|Input|Keeper|Input|100 K PD|
|GPIO_B0_09|C9|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO2.IO[9]|Input|Keeper|Input|100 K PD|



**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

106 

NXP Semiconductors 

**Package information and contact assignments** 

**Table 86. 12 x 12 mm functional contact assignments (continued)** 

|GPIO_B0_10|D9|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO2.IO[10]|Input|Keeper|Input|100 K PD|
|---|---|---|---|---|---|---|---|---|---|
|GPIO_B0_11|A10|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO2.IO[11]|Input|Keeper|Input|100 K PD|
|GPIO_B0_12|C10|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO2.IO[12]|Input|Keeper|Input|100 K PD|
|GPIO_B0_13|D10|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO2.IO[13]|Input|Keeper|Input|100 K PD|
|GPIO_B0_14|E10|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO2.IO[14]|Input|Keeper|Input|100 K PD|
|GPIO_B0_15|E11|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO2.IO[15]|Input|Keeper|Input|100 K PD|
|GPIO_B1_00|A11|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO2.IO[16]|Input|Keeper|Input|Keeper|
|GPIO_B1_01|B11|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO2.IO[17]|Input|Keeper|Input|Keeper|
|GPIO_B1_02|C11|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO2.IO[18]|Input|Keeper|Input|Keeper|
|GPIO_B1_03|D11|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO2.IO[19]|Input|Keeper|Input|Keeper|
|GPIO_B1_04|E12|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO2.IO[20]|Input|Keeper|Input|Keeper|
|GPIO_B1_05|D12|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO2.IO[21]|Input|Keeper|Input|Keeper|
|GPIO_B1_06|C12|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO2.IO[22]|Input|Keeper|Input|Keeper|
|GPIO_B1_07|B12|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO2.IO[23]|Input|Keeper|Input|Keeper|
|GPIO_B1_08|A12|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO2.IO[24]|Input|Keeper|Input|Keeper|
|GPIO_B1_09|A13|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO2.IO[25]|Input|Keeper|Input|Keeper|
|GPIO_B1_10|B13|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO2.IO[26]|Input|Keeper|Input|Keeper|
|GPIO_B1_11|C13|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO2.IO[27]|Input|Keeper|Input|Keeper|
|GPIO_B1_12|D13|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO2.IO[28]|Input|Keeper|Input|Keeper|
|GPIO_B1_13|D14|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO2.IO[29]|Input|Keeper|Input|Keeper|
|GPIO_B1_14|C14|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO2.IO[30]|Input|Keeper|Input|Keeper|



**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

NXP Semiconductors 

107 

**Package information and contact assignments** 

**Table 86. 12 x 12 mm functional contact assignments (continued)** 

|GPIO_B1_15|B14|NVCC_GPIO|Digital<br>GPIO|ALT5|GPIO2.IO[31]|Input|Keeper|Input|Keeper|
|---|---|---|---|---|---|---|---|---|---|
|GPIO_EMC_00|E3|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO4.IO[0]|Input|Keeper|Input|Keeper|
|GPIO_EMC_01|F3|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO4.IO[1]|Input|Keeper|Input|Keeper|
|GPIO_EMC_02|F4|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO4.IO[2]|Input|Keeper|Input|Keeper|
|GPIO_EMC_03|G4|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO4.IO[3]|Input|Keeper|Output1|Keeper|
|GPIO_EMC_04|F2|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO4.IO[4]|Input|Keeper|Input|Keeper|
|GPIO_EMC_05|G5|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO4.IO[5]|Input|Keeper|Input|Keeper|
|GPIO_EMC_06|H5|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO4.IO[6]|Input|Keeper|Input|Keeper|
|GPIO_EMC_07|H4|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO4.IO[7]|Input|Keeper|Input|Keeper|
|GPIO_EMC_08|H3|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO4.IO[8]|Input|Keeper|Input|Keeper|
|GPIO_EMC_09|C2|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO4.IO[9]|Input|Keeper|Input|Keeper|
|GPIO_EMC_10|G1|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO4.IO[10]|Input|Keeper|Input|Keeper|
|GPIO_EMC_11|G3|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO4.IO[11]|Input|Keeper|Input|Keeper|
|GPIO_EMC_12|H1|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO4.IO[12]|Input|Keeper|Input|Keeper|
|GPIO_EMC_13|A6|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO4.IO[13]|Input|Keeper|Input|Keeper|
|GPIO_EMC_14|B6|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO4.IO[14]|Input|Keeper|Input|Keeper|
|GPIO_EMC_15|B1|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO4.IO[15]|Input|Keeper|Input|Keeper|
|GPIO_EMC_16|A5|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO4.IO[16]|Input|Keeper|Input|Keeper|
|GPIO_EMC_17|A4|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO4.IO[17]|Input|Keeper|Input|Keeper|
|GPIO_EMC_18|B2|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO4.IO[18]|Input|Keeper|Input|Keeper|
|GPIO_EMC_19|B4|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO4.IO[19]|Input|Keeper|Input|Keeper|



**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

108 

NXP Semiconductors 

**Package information and contact assignments** 

**Table 86. 12 x 12 mm functional contact assignments (continued)** 

|GPIO_EMC_20|A3|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO4.IO[20]|Input|Keeper|Input|Keeper|
|---|---|---|---|---|---|---|---|---|---|
|GPIO_EMC_21|C1|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO4.IO[21]|Input|Keeper|Input|Keeper|
|GPIO_EMC_22|F1|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO4.IO[22]|Input|Keeper|Input|Keeper|
|GPIO_EMC_23|G2|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO4.IO[23]|Input|Keeper|Input|Keeper|
|GPIO_EMC_24|D3|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO4.IO[24]|Input|Keeper|Input|Keeper|
|GPIO_EMC_25|D2|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO4.IO[25]|Input|Keeper|Input|Keeper|
|GPIO_EMC_26|B3|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO4.IO[26]|Input|Keeper|Input|Keeper|
|GPIO_EMC_27|A2|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO4.IO[27]|Input|100 K PD|Input|100 K PD|
|GPIO_EMC_28|D1|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO4.IO[28]|Input|Keeper|Input|Keeper|
|GPIO_EMC_29|E1|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO4.IO[29]|Input|Keeper|Input|Keeper|
|GPIO_EMC_30|C6|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO4.IO[30]|Input|Keeper|Input|Keeper|
|GPIO_EMC_31|C5|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO4.IO[31]|Input|Keeper|Input|Keeper|
|GPIO_EMC_32|D5|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO3.IO[18]|Input|Keeper|Input|Keeper|
|GPIO_EMC_33|C4|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO3.IO[19]|Input|Keeper|Input|Keeper|
|GPIO_EMC_34|D4|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO3.IO[20]|Input|Keeper|Input|Keeper|
|GPIO_EMC_35|E5|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO3.IO[21]|Input|Keeper|Input|Keeper|
|GPIO_EMC_36|C3|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO3.IO[22]|Input|Keeper|Input|Keeper|
|GPIO_EMC_37|E4|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO3.IO[23]|Input|Keeper|Input|Keeper|
|GPIO_EMC_38|D6|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO3.IO[24]|Input|Keeper|Input|Keeper|
|GPIO_EMC_39|B7|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO3.IO[25]|Input|Keeper|Input|Keeper|
|GPIO_EMC_40|A7|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO3.IO[26]|Input|Keeper|Input|Keeper|



**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

NXP Semiconductors 

109 

**Package information and contact assignments** 

**Table 86. 12 x 12 mm functional contact assignments (continued)** 

|GPIO_EMC_41|C7|NVCC_EMC|Digital<br>GPIO|ALT5|GPIO3.IO[27]|Input|Keeper|Input|Keeper|
|---|---|---|---|---|---|---|---|---|---|
|GPIO_SD_B0_00|J4|NVCC_SD0|Digital<br>GPIO|ALT5|GPIO3.IO[12]|Input|Keeper|Input|Keeper|
|GPIO_SD_B0_01|J3|NVCC_SD0|Digital<br>GPIO|ALT5|GPIO3.IO[13]|Input|Keeper|Input|Keeper|
|GPIO_SD_B0_02|J1|NVCC_SD0|Digital<br>GPIO|ALT5|GPIO3.IO[14]|Input|Keeper|Input|Keeper|
|GPIO_SD_B0_03|K1|NVCC_SD0|Digital<br>GPIO|ALT5|GPIO3.IO[15]|Input|Keeper|Input|Keeper|
|GPIO_SD_B0_04|H2|NVCC_SD0|Digital<br>GPIO|ALT5|GPIO3.IO[16]|Input|Keeper|Input|Keeper|
|GPIO_SD_B0_05|J2|NVCC_SD0|Digital<br>GPIO|ALT5|GPIO3.IO[17]|Input|Keeper|Input|Keeper|
|GPIO_SD_B1_00|L5|NVCC_SD1|Digital<br>GPIO|ALT5|GPIO3.IO[0]|Input|Keeper|Input|Keeper|
|GPIO_SD_B1_01|M5|NVCC_SD1|Digital<br>GPIO|ALT5|GPIO3.IO[1]|Input|Keeper|Input|Keeper|
|GPIO_SD_B1_02|M3|NVCC_SD1|Digital<br>GPIO|ALT5|GPIO3.IO[2]|Input|Keeper|Input|Keeper|
|GPIO_SD_B1_03|M4|NVCC_SD1|Digital<br>GPIO|ALT5|GPIO3.IO[3]|Input|Keeper|Input|Keeper|
|GPIO_SD_B1_04|P2|NVCC_SD1|Digital<br>GPIO|ALT5|GPIO3.IO[4]|Input|Keeper|Input|Keeper|
|GPIO_SD_B1_05|N3|NVCC_SD1|Digital<br>GPIO|ALT5|GPIO3.IO[5]|Input|Keeper|Input|Keeper|
|GPIO_SD_B1_06|L3|NVCC_SD1|Digital<br>GPIO|ALT5|GPIO3.IO[6]|Input|Keeper|Input|Keeper|
|GPIO_SD_B1_07|L4|NVCC_SD1|Digital<br>GPIO|ALT5|GPIO3.IO[7]|Input|Keeper|Input|Keeper|
|GPIO_SD_B1_08|P3|NVCC_SD1|Digital<br>GPIO|ALT5|GPIO3.IO[8]|Input|Keeper|Input|Keeper|
|GPIO_SD_B1_09|N4|NVCC_SD1|Digital<br>GPIO|ALT5|GPIO3.IO[9]|Input|Keeper|Input|Keeper|
|GPIO_SD_B1_10|P4|NVCC_SD1|Digital<br>GPIO|ALT5|GPIO3.IO[01]|Input|Keeper|Input|Keeper|
|GPIO_SD_B1_11|P5|NVCC_SD1|Digital<br>GPIO|ALT5|GPIO3.IO[11]|Input|Keeper|Input|Keeper|
|ONOFF|M6|VDD_SNVS_I<br>N|Digital<br>GPIO|ALT0|ONOFF|Input|100 K PU|Input|100 K PU|
|PMIC_ON_REQ|K7|VDD_SNVS_I<br>N|Digital<br>GPIO|ALT0|SNVS_LP.PMIC_<br>ON_REQ|Output|100 K PU|Output|100 K PU|



**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

110 

NXP Semiconductors 

**Package information and contact assignments** 

**Table 86. 12 x 12 mm functional contact assignments (continued)** 

|PMIC_STBY_RE<br>Q|L7|VDD_SNVS_I<br>N|Digital<br>GPIO|ALT0|CCM.PMIC_VST<br>BY_REQ|Output|100 K PU<br>(PKE<br>disabled)|Output|100 K PU<br>(PKE<br>disabled)|
|---|---|---|---|---|---|---|---|---|---|
|POR_B|M7|VDD_SNVS_I<br>N|Digital<br>GPIO|ALT0|SRC.POR_B|Input|100 K PU|Input|100 K PU|
|RTC_XTALI|N9|—|—|—|—|—|—|—|—|
|RTC_XTALO|P9|—|—|—|—|—|—|—|—|
|TEST_MODE|K6|VDD_SNVS_I<br>N|Digital<br>GPIO|ALT0|TCU.TEST_MOD<br>E|Input|100 K PU|Input|100 K PU|
|USB_OTG1_CHD<br>_B|N12|—|—|—|—|—|—|—|—|
|USB_OTG1_DN|M8|—|—|—|—|—|—|—|—|
|USB_OTG1_DP|L8|—|—|—|—|—|—|—|—|
|USB_OTG1_VBU<br>S|N6|—|—|—|—|—|—|—|—|
|USB_OTG2_DN|N7|—|—|—|—|—|—|—|—|
|USB_OTG2_DP|P7|—|—|—|—|—|—|—|—|
|USB_OTG2_VBU<br>S|P6|—|—|—|—|—|—|—|—|
|XTALI|P11|—|—|—|—|—|—|—|—|
|XTALO|N11|—|—|—|—|—|—|—|—|
|WAKEUP|L6|VDD_SNVS_I<br>N|Digital<br>GPIO|ALT5|GPIO5.IO[0]|Input|100 K PU|Input|100 K PU|



1 This pin output is in a high level until the system reset is complete. 

**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

NXP Semiconductors 

111 

**Package information and contact assignments** 

## **6.2.3 12 x 12 mm, 0.8 mm pitch, ball map** 

Table 87 shows the 10 x 10 mm, 0.8 mm pitch ball map for the i.MX RT1060. 

**Table 87. 12 x 12 mm, 0.8 mm pitch, ball map** 

||**1**|**2**|**3**|**4**|**5**|**6**|**7**|**8**|**9**|**10**|**11**|**12**|**13**|**14**||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**A**|VSS|GPIO_EMC_27|GPIO_EMC_20|GPIO_EMC_17|GPIO_EMC_16|GPIO_EMC_13|GPIO_EMC_40|GPIO_B0_06|GPIO_B0_07|GPIO_B0_11|GPIO_B1_00|GPIO_B1_08|GPIO_B1_09|VSS|**A**|
|**B**|GPIO_EMC_15|GPIO_EMC_18|GPIO_EMC_26|GPIO_EMC_19|VSS|GPIO_EMC_14|GPIO_EMC_39|GPIO_B0_05|GPIO_B0_08|VSS|GPIO_B1_01|GPIO_B1_07|GPIO_B1_10|GPIO_B1_15|**B**|
|**C**|GPIO_EMC_21|GPIO_EMC_09|GPIO_EMC_36|GPIO_EMC_33|GPIO_EMC_31|GPIO_EMC_30|GPIO_EMC_41|GPIO_B0_04|GPIO_B0_09|GPIO_B0_12|GPIO_B1_02|GPIO_B1_06|GPIO_B1_11|GPIO_B1_14|**C**|
|**D**|GPIO_EMC_28|GPIO_EMC_25|GPIO_EMC_24|GPIO_EMC_34|GPIO_EMC_32|GPIO_EMC_38|GPIO_B0_00|GPIO_B0_03|GPIO_B0_10|GPIO_B0_13|GPIO_B1_03|GPIO_B1_05|GPIO_B1_12|GPIO_B1_13|**D**|
|**E**|GPIO_EMC_29|VSS|GPIO_EMC_00|GPIO_EMC_37|GPIO_EMC_35|NVCC_EMC|GPIO_B0_01|GPIO_B0_02|NVCC_GPIO|GPIO_B0_14|GPIO_B0_15|GPIO_B1_04|VSS|GPIO_AD_B0_06|**E**|
|**F**|GPIO_EMC_22|GPIO_EMC_04|GPIO_EMC_01|GPIO_EMC_02|NVCC_EMC|VDD_SOC_IN|VDD_SOC_IN|VDD_SOC_IN|VDD_SOC_IN|NVCC_GPIO|GPIO_AD_B0_04|GPIO_AD_B0_07|GPIO_AD_B0_08|GPIO_AD_B0_09|**F**|
|**G**|GPIO_EMC_10|GPIO_EMC_23|GPIO_EMC_11|GPIO_EMC_03|GPIO_EMC_05|VDD_SOC_IN|VSS|VSS|VDD_SOC_IN|GPIO_AD_B0_11|GPIO_AD_B0_03|GPIO_AD_B1_14|GPIO_AD_B0_10|GPIO_AD_B0_05|**G**|



**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

112 

NXP Semiconductors 

**Package information and contact assignments** 

**Table 87. 12 x 12 mm, 0.8 mm pitch, ball map (continued)** 

|**H**|GPIO_EMC_12|GPIO_SD_B0_04|GPIO_EMC_08|GPIO_EMC_07|GPIO_EMC_06|VDD_SOC_IN|VSS|VSS|VDD_SOC_IN|GPIO_AD_B0_01|GPIO_AD_B1_13|GPIO_AD_B1_12|GPIO_AD_B1_08|GPIO_AD_B0_14|**H**|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**J**|GPIO_SD_B0_02|GPIO_SD_B0_05|GPIO_SD_B0_01|GPIO_SD_B0_00|DCDC_SENSE|NVCC_SD0|VSS|VSS|VDD_SOC_IN|NVCC_GPIO|GPIO_AD_B1_00|GPIO_AD_B1_06|GPIO_AD_B1_11|GPIO_AD_B1_15|**J**|
|**K**|GPIO_SD_B0_03|VSS|DCDC_PSWITCH|DCDC__IN_Q|NVCC_SD1|TEST_MODE|PMIC_ON_REQ|VDD_USB_CAP|NGND_KEL0|GPIO_AD_B1_07|GPIO_AD_B1_01|GPIO_AD_B1_05|VSS|GPIO_AD_B0_12|**K**|
|**L**|DCDC_IN|DCDC_IN|GPIO_SD_B1_06|GPIO_SD_B1_07|GPIO_SD_B1_00|WAKEUP|PMIC_STBY_REQ|USB_OTG1_DP|VSS|GPIO_AD_B0_15|GPIO_AD_B1_02|GPIO_AD_B1_04|GPIO_AD_B1_10|GPIO_AD_B0_13|**L**|
|**M**|DCDC_LP|DCDC_LP|GPIO_SD_B1_02|GPIO_SD_B1_03|GPIO_SD_B1_01|ONOFF|POR_B|USB_OTG1_DN|VDD_SNVS_IN|VDD_SNVS_CAP|GPIO_AD_B0_02|GPIO_AD_B1_03|GPIO_AD_B1_09|GPIO_AD_B0_00|**M**|
|**N**|DCDC_GND|DCDC_GND|GPIO_SD_B1_05|GPIO_SD_B1_09|VSS|USB_OTG1_VBUS|USB_OTG2_DN|VSS|RTC_XTALI|GPANAIO|XTALO|USB_OTG1_CHD_B|CCM_CLK1_P|VDDA_ADC_3P3|**N**|
|**P**|VSS|GPIO_SD_B1_04|GPIO_SD_B1_08|GPIO_SD_B1_10|GPIO_SD_B1_11|USB_OTG2_VBUS|USB_OTG2_DP|VDD_HIGH_CAP|RTC_XTALO|NVCC_PLL|XTALI|VDD_HIGH_IN|CCM_CLK1_N|VSS|**P**|
||**1**|**2**|**3**|**4**|**5**|**6**|**7**|**8**|**9**|**10**|**11**|**12**|**13**|**14**||



**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

NXP Semiconductors 

113 

**Revision history** 

## **7 Revision history** 

## Table 88 provides a revision history for this data sheet. 

## **Table 88. i.MX RT1060 Data Sheet document revision history** 

|**Rev.**<br>**Number**|**Date**|**Substantive Change(s)**|
|---|---|---|
|Rev.4|04/2024|• InFigure 2, "i.MX RT1060 system block diagram":<br>– Added FlexIO1 and FlexIO2<br>– Updated FlexPWM (8-Channel x4) to (4-Channel x4).<br>– Updated Internal memory 96KB ROM to 128KB ROM, updated “GP Timer” instance to 2 and<br>removed ”Shared with TCM”<br>• UpdatedFigure 1, "Part number nomenclature—i.MX RT10XX family"<br>• Interchanged the Min. and Max. values of spec “System frequency/Bus frequency” inTable 10,<br>Operating ranges<br>• Added FlexIO3 inTable 2, i.MX RT1060 modules list.<br>• Added note inTable 3, Special signal considerations<br>• Added new part numbers “MIMXRT106VDVL6B”, “MIMXRT106CDVL6B”, “MIMXRT106DDVL6B”,<br>“MIMXRT106PDVL6B” and their relevant information inTable 1, Ordering information<br>• InTable 83, 10 x 10 mm functional contact assignmentsandTable 86, 12 x 12 mm functional contact<br>assignmentsfor “GPIO_AD_B0_10”, updated the default status to output.<br>• InSection 4.2.1.1, Power-up sequenceremoved “VDDA_ADC_3P3” instance from note<br>”USB_OTG1_VBUS and USB_OTG2_VBUS are not part of the power....”|
|Rev. 3|03/2022|• Updated theFigure 1, "Part number nomenclature—i.MX RT10XX family"<br>• Updated the part number for MIMXRT106LDVL6A and MIMXRT106LDVL6B in theTable 1, Ordering<br>information<br>• Updated theSection 4.2.1.1, Power-up sequence<br>• Updated for FlexSPI x2 in theSection 3, Modules List<br>• Updated theFigure 19, "FlexSPI input timing in SDR mode where FlexSPIn_MCR0[RXCLKSRC] =<br>0X0, 0X1"<br>• Updated row 6 in theTable 57, LPSPI Master mode timing<br>• Updated theTable 55, 12-bit ADC characteristics (VREFH = VDDA, VREFL = VSSAD)<br>• Updated theFigure 2, "i.MX RT1060 system block diagram"|
|Rev. 2|03/2021|• Added a new part number in theTable 1, Ordering information<br>• Updated theFigure 1, "Part number nomenclature—i.MX RT10XX family"<br>• Updated the baud rate of LPUART in theTable 2, i.MX RT1060 modules list<br>• Updated the descriptions of TEST_MODE in theTable 3, Special signal considerations<br>• Added system frequencies and bus frequencies inTable 10, Operating ranges; update the maximum<br>value of 3.3 V NVCC_EMC in theTable 10, Operating ranges<br>• Updated the maximum values of low-level output currents in theTable 22, Single voltage GPIO DC<br>parameters<br>• Added Default setting on reset columns and a footnote in theTable 83, 10 x 10 mm functional contact<br>assignmentsandTable 86, 12 x 12 mm functional contact assignments|
|Rev. 1|07/2020|• Changed the MPCore to core in theSection 1.1, Features<br>• Added new part numbers in theTable 1, Ordering information<br>• Updated theFigure 1, "Part number nomenclature—i.MX RT10XX family"<br>• Updated the frequency of RTC OSC in theTable 2, i.MX RT1060 modules list<br>• Updated conditions and maximum current of DCDC_IN in theTable 12, Maximum supply currents<br>• Added a restrictions in theSection 4.2.1.1, Power-up sequence<br>• Added IOHand IOLin theTable 22, Single voltage GPIO DC parameters<br>• Updated the minimum and maximum values in theTable 33, SEMC output timing in SYNC mode|



**i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024** 

114 

NXP Semiconductors 

## **Table 88. i.MX RT1060 Data Sheet document revision history (continued)** 

|**Rev.**<br>**Number**|**Date**|**Substantive Change(s)**|
|---|---|---|
|Rev. 0.2|02/2020|• Updated the SPI NAND Flash in theSection 1.1, Features<br>• Updated the features of RT1062 in theTable 1, Ordering information<br>• Updated theTable 81, Boot through UART1and removed the Table, Boot through UART2<br>• Updated the figure and table numbers in theSection 6.2, 12 x 12 mm package information<br>• Updated theFigure 53, "10 x 10 mm BGA, case x package top, bottom, and side Views"and<br>Figure 54, "12 x 12 mm BGA, case x package top, bottom, and side Views"|
|Rev. 0.1|04/2019|• Updated ADC information and removed DAC fromSection 1.1, FeaturesandFigure 2, "i.MX RT1060<br>system block diagram"<br>• Added a new part number in theTable 1, Ordering information<br>• Updated the RT website link in theSection 1.2, Ordering information<br>• Removed tamper detection from theTable 2, i.MX RT1060 modules list<br>• Updated the on-chip termination values of JTAG_TCK and JTAG_MOD in theTable 4, JTAG<br>Controller interface summary<br>• Updated the maximum value of VDD_SOC_IN in theTable 7, Absolute maximum ratings<br>• Changed 528 MHz PLL to System PLL in theTable 16, System PLL’s electrical parameters<br>• Changed 480 MHz PLL to USB PLL in theTable 18, USB PLL’s electrical parameters<br>• Updated the VDD name of supply voltage conditions column in theTable 54, 12-bit ADC operating<br>conditions<br>• Added theFigure 36, "Minimum Sample Time Vs Ras (Cas = 2pF)",Figure 37, "Minimum Sample<br>Time Vs Ras (Cas = 5 pF)", andFigure 38, "Minimum Sample Time Vs Ras (Cas = 10 pF)"in the<br>Section 4.8.2, A/D converter<br>• Updated theSection 4.9.1, LPSPI timing parameters|
|Rev. 0|08/2018|• Initial version|



NXP Semiconductors 

Legal information 

## Legal information 

## Data sheet status 

|Document status[1][2]|Product status[3]|Definition|
|---|---|---|
|Objective [short] data sheet|Development|This document contains data from the objective specification for product<br>development.|
|Preliminary [short] data sheet|Qualification|This document contains data from the preliminary specification.|
|Product [short] data sheet|Production|This document contains the product specification.|



[1] Please consult the most recently issued document before initiating or completing a design. 

- [2] The term 'short data sheet' is explained in section "Definitions". 

[3] The product status of device(s) described in this document may have changed since this document was published and may differ in case of multiple devices. The latest product status information is available on the Internet at URL https://www.nxp.com. 

## Definitions 

Draft — A draft status on a document indicates that the content is still under internal review and subject to formal approval, which may result in modifications or additions. NXP Semiconductors does not give any representations or warranties as to the accuracy or completeness of information included in a draft version of a document and shall have no liability for the consequences of use of such information. 

Short data sheet — A short data sheet is an extract from a full data sheet with the same product type number(s) and title. A short data sheet is intended for quick reference only and should not be relied upon to contain detailed and full information. For detailed and full information see the relevant full data sheet, which is available on request via the local NXP Semiconductors sales office. In case of any inconsistency or conflict with the short data sheet, the full data sheet shall prevail. 

Product specification — The information and data provided in a Product data sheet shall define the specification of the product as agreed between NXP Semiconductors and its customer, unless NXP Semiconductors and customer have explicitly agreed otherwise in writing. In no event however, shall an agreement be valid in which the NXP Semiconductors product is deemed to offer functions and qualities beyond those described in the Product data sheet. 

## Disclaimers 

Limited warranty and liability — Information in this document is believed to be accurate and reliable. However, NXP Semiconductors does not give any representations or warranties, expressed or implied, as to the accuracy or completeness of such information and shall have no liability for the consequences of use of such information. NXP Semiconductors takes no responsibility for the content in this document if provided by an information source outside of NXP Semiconductors. 

In no event shall NXP Semiconductors be liable for any indirect, incidental, punitive, special or consequential damages (including - without limitation - lost profits, lost savings, business interruption, costs related to the removal or replacement of any products or rework charges) whether or not such damages are based on tort (including negligence), warranty, breach of contract or any other legal theory. 

Notwithstanding any damages that customer might incur for any reason whatsoever, NXP Semiconductors’ aggregate and cumulative liability towards customer for the products described herein shall be limited in accordance with the Terms and conditions of commercial sale of NXP Semiconductors. 

Right to make changes — NXP Semiconductors reserves the right to make changes to information published in this document, including without limitation specifications and product descriptions, at any time and without notice. This document supersedes and replaces all information supplied prior to the publication hereof. 

Suitability for use — NXP Semiconductors products are not designed, authorized or warranted to be suitable for use in life support, life-critical or safety-critical systems or equipment, nor in applications where failure or malfunction of an NXP Semiconductors product can reasonably be expected to result in personal injury, death or severe property or environmental damage. NXP Semiconductors and its suppliers accept no liability for inclusion and/or use of NXP Semiconductors products in such equipment or applications and therefore such inclusion and/or use is at the customer’s own risk. 

i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024 

Data Sheet: Technical Data 

NXP Semiconductors 

Legal information 

Applications — Applications that are described herein for any of these products are for illustrative purposes only. NXP Semiconductors makes no representation or warranty that such applications will be suitable for the specified use without further testing or modification. 

Customers are responsible for the design and operation of their applications and products using NXP Semiconductors products, and NXP Semiconductors accepts no liability for any assistance with applications or customer product design. It is customer’s sole responsibility to determine whether the NXP Semiconductors product is suitable and fit for the customer’s applications and products planned, as well as for the planned application and use of customer’s third party customer(s). Customers should provide appropriate design and operating safeguards to minimize the risks associated with their applications and products. 

NXP Semiconductors does not accept any liability related to any default, damage, costs or problem which is based on any weakness or default in the customer’s applications or products, or the application or use by customer’s third party customer(s). Customer is responsible for doing all necessary testing for the customer’s applications and products using NXP Semiconductors products in order to avoid a default of the applications and the products or of the application or use by customer’s third party customer(s). NXP does not accept any liability in this respect. 

Limiting values — Stress above one or more limiting values (as defined in the Absolute Maximum Ratings System of IEC 60134) will cause permanent damage to the device. Limiting values are stress ratings only and (proper) operation of the device at these or any other conditions above those given in the Recommended operating conditions section (if present) or the Characteristics sections of this document is not warranted. Constant or repeated exposure to limiting values will permanently and irreversibly affect the quality and reliability of the device. 

Terms and conditions of commercial sale — NXP Semiconductors products are sold subject to the general terms and conditions of commercial sale, as published at https://www.nxp.com/profile/terms, unless otherwise agreed in a valid written individual agreement. In case an individual agreement is concluded only the terms and conditions of the respective agreement shall apply. NXP Semiconductors hereby expressly objects to applying the customer’s general terms and conditions with regard to the purchase of NXP Semiconductors products by customer. 

No offer to sell or license — Nothing in this document may be interpreted or construed as an offer to sell products that is open for acceptance or the grant, conveyance or implication of any license under any copyrights, patents or other industrial or intellectual property rights. 

Bare die — All die are tested on compliance with their related technical specifications as stated in this data sheet up to the point of wafer sawing and are handled in accordance with the NXP Semiconductors storage and transportation conditions. If there are data sheet limits not guaranteed, these will be separately indicated in the data sheet. There are no post-packing tests performed on individual die or wafers. 

NXP Semiconductors has no control of third party procedures in the sawing, handling, packing or assembly of the die. Accordingly, NXP Semiconductors assumes no liability for device functionality or performance of the die or systems after third party sawing, handling, packing or assembly of the die. It is the responsibility of the customer to test and qualify their application in which the die is used. 

All die sales are conditioned upon and subject to the customer entering into a written die sale agreement with NXP Semiconductors through its legal department. 

Quick reference data — The Quick reference data is an extract of the product data given in the Limiting values and Characteristics sections of this document, and as such is not complete, exhaustive or legally binding. 

Export control — This document as well as the item(s) described herein may be subject to export control regulations. Export might require a prior authorization from competent authorities. 

Suitability for use in non-automotive qualified products — Unless this document expressly states that this specific NXP Semiconductors product is automotive qualified, the product is not suitable for automotive use. It is neither qualified nor tested in accordance with automotive testing or application requirements. NXP Semiconductors accepts no liability for inclusion and/or use of non-automotive qualified products in automotive equipment or applications. 

In the event that customer uses the product for design-in and use in automotive applications to automotive specifications and standards, customer (a) shall use the product without NXP Semiconductors’ warranty of the product for such automotive applications, use and specifications, and (b) whenever customer uses the product for automotive applications beyond NXP Semiconductors’ specifications such use shall be solely at customer’s own risk, and (c) customer fully indemnifies NXP Semiconductors for any liability, damages or failed product claims resulting from customer design and use of the product for automotive applications beyond NXP Semiconductors’ standard warranty and NXP Semiconductors’ product specifications. 

Translations — A non-English (translated) version of a document, including the legal information in that document, is for reference only. The English version shall prevail in case of any discrepancy between the translated and English versions. 

i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024 

Data Sheet: Technical Data 

NXP Semiconductors 

Legal information 

Security — Customer understands that all NXP products may be subject to unidentified vulnerabilities or may support established security standards or specifications with known limitations. Customer is responsible for the design and operation of its applications and products throughout their lifecycles to reduce the effect of these vulnerabilities on customer’s applications and products. Customer’s responsibility also extends to other open and/or proprietary technologies supported by NXP products for use in customer’s applications. NXP accepts no liability for any vulnerability. Customer should regularly check security updates from NXP and follow up appropriately. 

Customer shall select products with security features that best meet rules, regulations, and standards of the intended application and make the ultimate design decisions regarding its products and is solely responsible for compliance with all legal, regulatory, and security related requirements concerning its products, regardless of any information or support that may be provided by NXP. 

NXP has a Product Security Incident Response Team (PSIRT) (reachable at PSIRT@nxp.com) that manages the investigation, reporting, and solution release to security vulnerabilities of NXP products. 

NXP B.V. — NXP B.V. is not an operating company and it does not distribute or sell products. 

## Trademarks 

Notice: All referenced brands, product names, service names, and trademarks are the property of their respective owners. 

NXP — wordmark and logo are trademarks of NXP B.V. 

AMBA, Arm, Arm7, Arm7TDMI, Arm9, Arm11, Artisan, big.LITTLE, Cordio, CoreLink, CoreSight, Cortex, DesignStart, DynamIQ, Jazelle, Keil, Mali, Mbed, Mbed Enabled, NEON, POP, RealView, SecurCore, Socrates, Thumb, TrustZone, ULINK, ULINK2, ULINK-ME, ULINK-PLUS, ULINKpro, μVision, Versatile — are trademarks and/or registered trademarks of Arm Limited (or its subsidiaries or affiliates) in the US and/or elsewhere. The related technology may be protected by any or all of patents, copyrights, designs and trade secrets. All rights reserved. 

Airfast — is a trademark of NXP B.V. 

CodeWarrior — is a trademark of NXP B.V. ColdFire — is a trademark of NXP B.V. ColdFire+ — is a trademark of NXP B.V. CoolFlux — is a trademark of NXP B.V. DESFire — is a trademark of NXP B.V. EdgeLock — is a trademark of NXP B.V. EdgeScale — is a trademark of NXP B.V. eIQ — is a trademark of NXP B.V. Freescale — is a trademark of NXP B.V. GreenChip — is a trademark of NXP B.V. HITAG — is a trademark of NXP B.V. 

ICODE and I-CODE — are trademarks of NXP B.V. 

Immersiv3D — is a trademark of NXP B.V. JCOP — is a trademark of NXP B.V. Kinetis — is a trademark of NXP B.V. 

Layerscape — is a trademark of NXP B.V. 

MagniV — is a trademark of NXP B.V. 

Mantis — is a trademark of NXP B.V. 

MIFARE — is a trademark of NXP B.V. MIFARE Classic — is a trademark of NXP B.V. MIFARE4Mobile — is a trademark of NXP B.V. 

MIFARE Plus — is a trademark of NXP B.V. 

MIFARE Ultralight — is a trademark of NXP B.V. 

MiGLO — wordmark and logo are trademarks of NXP B.V. 

NTAG — is a trademark of NXP B.V. 

NXP SECURE CONNECTIONS FOR A SMARTER WORLD — is a trademark of NXP B.V. 

Oracle and Java — are registered trademarks of Oracle and/or its affiliates. PEG — is a trademark of NXP B.V. 

Processor Expert — is a trademark of NXP B.V. QorIQ — is a trademark of NXP B.V. QorIQ Qonverge — is a trademark of NXP B.V. RoadLINK — wordmark and logo are trademarks of NXP B.V. 

SafeAssure — is a trademark of NXP B.V. 

SafeAssure — logo is a trademark of NXP B.V. 

SmartMX — is a trademark of NXP B.V. 

Synopsys — Portions Copyright[©] 2018-2022 Synopsys, Inc. Used with permission. All rights reserved. 

Tower — is a trademark of NXP B.V. UCODE — is a trademark of NXP B.V. VortiQa — is a trademark of NXP B.V. 

i.MX RT1060 Crossover Processors for Consumer Products, Rev. 4, 04/2024 

Data Sheet: Technical Data 

**==> picture [8 x 8] intentionally omitted <==**

Please be aware that important notices concerning this document and the product(s) described herein, have been included in section 'Legal information'. 

© NXP B.V. 2024. 

All rights reserved. 

For more information, please visit: https://www.nxp.com 

Date of release: 04/2024 

Document identifier: IMXRT1060CEC 

