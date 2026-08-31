# Athom ESPHome Device Configurations

This repository contains ESPHome YAML configurations for Athom ESP32, ESP32-C3, and ESP32-C5 devices.

## Quick Links

- Official website: <https://www.athom.tech/>
- AliExpress store: <https://iotorero.aliexpress.com/>
- Web firmware installer: <https://athom-tech.github.io/esp32-configs/>
- Releases: <https://github.com/athom-tech/esp32-configs/releases>
- ESPHome documentation: <https://esphome.io/>
- ESP Web Tools: <https://esphome.github.io/esp-web-tools/>
- Home Assistant: <https://www.home-assistant.io/>

## Supported Devices

Each file contains a `dashboard_import` URL in the form `github://athom-tech/esp32-configs/<file>.yaml`.

| YAML | Device name | Board target | Primary function |
| --- | --- | --- | --- |
| `athom-1gang-switch.yaml` | 1Gang Switch | `esp32-c3-devkitm-1` | Single-gang wall switch with button, relay/light output, status LED, and power-on state control. |
| `athom-2gang-switch.yaml` | 2Gang Switch | `esp32-c3-devkitm-1` | Two-gang wall switch with two buttons, two light outputs, status LED, and power-on state control. |
| `athom-3gang-switch.yaml` | 3Gang Switch | `esp32-c3-devkitm-1` | Three-gang wall switch with three buttons, three light outputs, status LED, and power-on state control. |
| `athom-4gang-switch.yaml` | 4Gang Switch | `esp32-c3-devkitm-1` | Four-gang wall switch with four buttons, four light outputs, status LED, and power-on state control. |
| `athom-2ch-relay-board.yaml` | Athom 2CH Relay Board | `esp32dev` | Two-channel relay board with local buttons, RF receiver support, and status telemetry. |
| `athom-4ch-relay-board.yaml` | Athom 4CH Relay Board | `esp32dev` | Four-channel relay board with local buttons, RF receiver support, and status telemetry. |
| `athom-8ch-relay-board.yaml` | Athom 8CH Relay Board | `esp32dev` | Eight-channel relay board with local buttons, RF receiver support, and status telemetry. |
| `athom-dual-smart-plug-v3.yaml` | Athom Dual Plug V3 | `esp32-c3-devkitm-1` | Dual smart plug with independent relay control, per-channel and aggregate power monitoring, persistent energy totals, and energy reset controls. |
| `athom-energy-monitor-x2.yaml` | Athom Energy Meter | `esp32-c3-devkitm-1` | Two-channel energy monitor using the local `bl0906` component. |
| `athom-energy-monitor-x6.yaml` | Athom Energy Meter | `esp32-c3-devkitm-1` | Six-channel energy monitor using the local `bl0906` component. |
| `athom-garage-door.yaml` | Athom Garage Door | `esp32-c3-devkitm-1` | Garage door opener with relay control, door state inputs, template cover, and status LED. |
| `athom-ld2450-sensor.yaml` | PS02C3MZ Sensor | `esp32-c3-devkitm-1` | LD2450 mmWave presence sensor with target tracking, zones, light sensor, and status LED. |
| `athom-mini-relay-v2.yaml` | Athom Mini Relay V2 | `esp32-c3-devkitm-1` | Mini relay with local switch input, relay output, status LED, and power monitoring. |
| `athom-presence-sensor-v3.yaml` | Athom Presence Sensor | `esp32-c3-devkitm-1` | mmWave presence sensor with light sensing, zone controls, UART/I2C peripherals, and status LED. |
| `athom-rf-ir-remote.yaml` | Athom RF IR Remote | `esp32dev` | RF/IR remote bridge with 10 IR learning slots, 16 RF433 learning slots, transmission controls, and status telemetry. |
| `athom-rgbcw-bulb.yaml` | Athom RGBCW Bulb | `esp32-c3-devkitm-1` | RGBCW bulb with RGBWW output, power-on state control, and switchable ESP-NOW remote pairing and control. |
| `athom-rgbcw-light.yaml` | Athom RGBCW Bulb | `esp32-c3-devkitm-1` | 12W RGBCW light variant with alternate GPIO mapping and switchable ESP-NOW remote pairing and control. |
| `athom-scd40-sensor.yaml` | Athom C02 Sensor | `esp32-c3-devkitm-1` | SCD40 CO2, temperature, and humidity sensor with status light control. |
| `athom-sht40-sensor.yaml` | Athom Temperature Humidity Sensor | `esp32-c3-devkitm-1` | SHT40 temperature and humidity sensor with calibration offsets and status light control. |
| `athom-smart-plug.yaml` | Athom Plug V3 | `esp32-c3-devkitm-1` | Smart plug with relay control, physical button, status LED, and power monitoring. |
| `athom-smart-plug-v5.yaml` | Athom Plug V5 | `esp32-c5-devkitc1-n4` | ESP32-C5 smart plug with relay control, physical button, status LED, and power monitoring. |
| `athom-wall-outlet-v3.yaml` | Athom Wall Outlet | `esp32-c3-devkitm-1` | Wall outlet with relay control, physical button, status LED, and power monitoring. |
| `athom-zigbee-gateway.yaml` | Athom Zigbee Gateway | `esp32dev` | Zigbee gateway configuration with UART bridge controls, boot/reset switches, and status LED. |

## Installation

### Option 1: Install Pre-Built Firmware

Use the GitHub Pages installer when you want the simplest first-time flash.

1. Open <https://athom-tech.github.io/esp32-configs/> in a browser that supports Web Serial, such as Chrome or Edge.
2. Connect the device over USB.
3. Select the firmware version and device.
4. Click the install button and follow the browser prompts.
5. After flashing, provision Wi-Fi when prompted by the device or ESP Web Tools.

The installer reads firmware manifests and binaries published by the release workflow. If the installer says firmware is unavailable, wait for the firmware release and Pages workflow to complete.

### Option 2: Import into ESPHome Dashboard

Each YAML file includes a `dashboard_import` entry. In ESPHome Dashboard, import the device configuration with this pattern:

```text
github://athom-tech/esp32-configs/<file>.yaml
```

For example:

```text
github://athom-tech/esp32-configs/athom-smart-plug.yaml
```

After import, adjust substitutions such as the device name, friendly name, room, DNS domain, and restore behavior where the YAML exposes them.

### Option 3: Build and Flash Locally

Install ESPHome and build a selected configuration from the repository root:

```sh
esphome compile athom-smart-plug.yaml
```

Flash over USB for a first install:

```sh
esphome run athom-smart-plug.yaml
```

After the device is online, ESPHome can usually update it over the network:

```sh
esphome upload athom-smart-plug.yaml --device athom-smart-plug-v3.local
```

Use the actual YAML file and hostname for your device.

### OTA Updates

The YAML files enable standard ESPHome OTA updates. Once a device has been flashed and is reachable on Wi-Fi, future updates can be installed from ESPHome Dashboard or with the ESPHome CLI.

Most configurations also expose a managed `Firmware Update` entity in Home Assistant. This entity checks the device-specific manifest published on GitHub Pages and can install released firmware over HTTP. The ESP32-C5 smart plug currently uses standard ESPHome OTA only.

#### Disabling the Managed Firmware Update

The managed update feature is provided by the `ota` `http_request` platform, the `http_request` component, and the `update` `Firmware Update` entity. On some ESPHome versions the periodic HTTP manifest checks can make the device's status LED flash constantly (see [issue #88](https://github.com/athom-tech/esp32-configs/issues/88)).

Because devices are imported through `packages:`, do not edit the Athom YAML directly. Instead, add these overrides to your **own** configuration (the file that imports the package) to remove the managed update components:

```yaml
ota:
  - id: !remove ota_http_request

update:
  - id: !remove update_http_request

http_request: !remove
```

Standard ESPHome OTA (the `ota_esphome` platform) still works after this — only the managed HTTP-manifest updating and its `Firmware Update` entity are removed. To re-enable the feature later, delete this override block.

If OTA fails, confirm that:

- The device is powered and connected to the same network as ESPHome.
- The configured hostname resolves through mDNS or local DNS.
- The YAML still matches the hardware variant already installed on the device.
- The device has enough free memory and a stable Wi-Fi signal during upload.

## Configuration Notes

- Most YAML files use `substitutions` for `name`, `friendly_name`, room metadata, project metadata, restore behavior, and optional DNS domain settings.
- Most Wi-Fi-based configurations include fallback access point and captive portal support so a device can expose a temporary setup network if it cannot join the configured network.
- ESPHome API is enabled for Home Assistant integration.
- OTA and web server support are enabled in the device configurations.
- Common diagnostic entities include status, uptime, Wi-Fi signal, and restart/factory-reset style buttons.
- Power-monitoring devices expose voltage, current, power, energy, total energy, and related calculated sensors where supported by the hardware.
- The dual smart plug exposes per-channel measurements plus total current and total active power, persists per-channel and aggregate energy totals, and provides controls to reset those totals.
- Presence and LD2450-based devices expose target, zone, presence, illuminance, and radar control entities.
- Devices are expected to be discovered by Home Assistant through the ESPHome integration after they are on the network.

## Troubleshooting

### Browser or USB Device Is Not Detected

Use Chrome or Edge for the web installer because Web Serial support is required. Use a data-capable USB cable, confirm that the device is in flashing mode if required, and close other serial monitors before installing.

### The Wrong Firmware Was Installed

Select the YAML or installer device entry that matches the exact Athom hardware variant. Similar devices may use different GPIO mappings, especially light and plug revisions.

### Wi-Fi Setup Does Not Complete

Move the device closer to the access point, check credentials, and look for the fallback access point exposed by the device. If the YAML uses a custom DNS domain, confirm that the hostname you are using matches the configured `name` and domain.

### Home Assistant Does Not Discover the Device

Make sure the device and Home Assistant are on the same network segment, then add it manually from Home Assistant's ESPHome integration if automatic discovery does not appear.

### OTA Update Fails

Use the installed device's matching YAML, verify network reachability, and try a USB flash if the device is offline or running incompatible firmware.

### Status LED Flashes Constantly

On some ESPHome versions, the periodic HTTP requests from the managed firmware-update feature can make the status LED flash rapidly and constantly, even though the device otherwise works and stays connected to Home Assistant. Disable the managed update as described in [Disabling the Managed Firmware Update](#disabling-the-managed-firmware-update).

### Local Build Fails

Update ESPHome, check the error message for missing dependencies or component compatibility, and compare the failing YAML with nearby device configurations that build successfully. The CI workflow is the reference for the ESPHome versions expected to build.
