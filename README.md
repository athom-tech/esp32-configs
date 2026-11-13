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
| `athom-dual-smart-plug-v3.yaml` | Athom Dual Plug V3 | `esp32-c3-devkitm-1` | Dual-channel smart plug with independent relay control and buttons, dual-channel energy metering. |
| `athom-energy-monitor-x2.yaml` | Athom Energy Meter | `esp32-c3-devkitm-1` | Two-channel energy monitor using the local `bl0906` component. |
| `athom-energy-monitor-x6.yaml` | Athom Energy Meter | `esp32-c3-devkitm-1` | Six-channel energy monitor using the local `bl0906` component. |
| `athom-garage-door.yaml` | Athom Garage Door | `esp32-c3-devkitm-1` | Garage door opener with relay control, door state inputs, template cover, and status LED. |
| `athom-ld2450-sensor.yaml` | PS02C3MZ Sensor | `esp32-c3-devkitm-1` | LD2450 mmWave presence sensor with target tracking, zones, light sensor, and status LED. |
| `athom-mini-relay-v2.yaml` | Athom Mini Relay V2 | `esp32-c3-devkitm-1` | Mini relay with local switch input, relay output, status LED, and power monitoring. |
| `athom-presence-sensor-v3.yaml` | Athom Presence Sensor | `esp32-c3-devkitm-1` | mmWave presence sensor with light sensing, zone controls, UART/I2C peripherals, and status LED. |
| `athom-rf-ir-remote.yaml` | Athom RF IR Remote | `esp32dev` | RF/IR remote bridge with 10 IR learning slots, 16 RF433 learning slots, transmission controls, and status telemetry. |
| `athom-rf-ir-remote-pro.yaml` | Athom RF433 IR Remote Pro | `esp32dev` | RF433/IR remote bridge with learning slots, IR climate, and in-place switching to the SHT40/SCD40 firmware variants below. |
| `athom-rf-ir-remote-pro-sht40.yaml` | Athom RF433 IR Remote Pro + SHT40 | `esp32dev` | RF433 IR Remote Pro firmware with an external SHT40 temperature and humidity sensor and calibration offsets. |
| `athom-rf-ir-remote-pro-scd40.yaml` | Athom RF433 IR Remote Pro + SCD40 | `esp32dev` | RF433 IR Remote Pro firmware with an external SCD40 CO2, temperature, and humidity sensor and calibration offsets. |
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
- The dual smart plug performs dual-channel energy metering with the `bl0939` chip over UART, exposing per-channel voltage, current, active power, energy, and daily energy, plus total current, total active power, and total energy. It persists per-channel and aggregate energy totals across reboots and provides buttons to reset each total. A configurable current limit (16 A by default) trips the affected channel off for overcurrent protection, a `Power On State` selector sets the boot behaviour (always off, always on, or restore previous state), and each channel can be toggled with its physical button (a 4-second hold triggers factory reset).
- Presence and LD2450-based devices expose target, zone, presence, illuminance, and radar control entities.
- Devices are expected to be discovered by Home Assistant through the ESPHome integration after they are on the network.

### Taking Control: Extending or Removing Configuration

Each device configuration gives explicit IDs to its entities and components wherever the ESPHome schema supports them, including internal entities, nested sensor outputs, I2C/UART buses, and services. These are ESPHome configuration IDs, separate from Home Assistant entity IDs. Existing IDs retain their original spelling and capitalization; an ID only needs to be unique within one device's configuration.

After taking control, keep your changes in the configuration that imports the Athom package. Find the exact ID in your device's YAML and use `!extend` or `!remove` for list entries. For example, this renames the Wi-Fi percentage sensor and removes the restart button from a smart plug:

```yaml
packages:
  athom: !include athom-smart-plug.yaml

sensor:
  - id: !extend wifi_signal_percent
    name: "WiFi Signal Percentage"

button:
  - id: !remove id_restart
```

The local `!include` example assumes the device YAML is beside your configuration. If your configuration already imports the package, keep that existing import instead.

For nested outputs, extend the parent component and edit or remove the child by its configuration key. Add this to the same smart-plug configuration to rename its current sensor and remove its power-factor sensor:

```yaml
sensor:
  - id: !extend athom_cse7766
    current:
      name: "Current Draw"
    power_factor: !remove
```

Combine entries under one `sensor:` key when using both examples. Mapping-style services merge by their top-level key: for example, `web_server: {port: 8080}` changes the port, and `web_server: !remove` removes that service. Configuration groups and platform wrappers that do not accept an `id` keep their schema-defined structure.

Common IDs include `id_status`, `wifi_signal_percent`, `id_restart`, `id_safe_mode`, `ip_address`, `ssid`, and `mac_address`. Previously unnamed buses use `i2c_bus` or `uart_bus`; services use IDs such as `api_component` and `wifi_component`. Existing bus and entity IDs may differ between devices, so always check the selected YAML.

When removing an entity or component, also remove or update anything that depends on it, such as `id(...)` lambdas, automation actions, `source_id`, `power_id`, or bus references. Removing a bus also requires handling the peripherals that use it. Validate your final configuration with `esphome config <your-device>.yaml`. See the [ESPHome packages documentation](https://esphome.io/components/packages/) for the supported merge, extension, and removal syntax.

### Wall Switches: Programmable Button Mode

The one-, two-, three-, and four-gang switch configurations expose button mode selectors in Home Assistant and the device's web interface. Each physical button has its own mode selector and event entity:

| Configuration | Mode selectors | Event entities |
| --- | --- | --- |
| `athom-1gang-switch.yaml` | **Button Mode** | **Button Event** |
| `athom-2gang-switch.yaml` | **Button1 Mode**, **Button2 Mode** | **Button1 Event**, **Button2 Event** |
| `athom-3gang-switch.yaml` | **Button1 Mode** through **Button3 Mode** | **Button1 Event** through **Button3 Event** |
| `athom-4gang-switch.yaml` | **Button1 Mode** through **Button4 Mode** | **Button1 Event** through **Button4 Event** |

Every button defaults to **Relay**, which keeps the existing behavior: a short press (up to 0.5 seconds, followed by at least 0.2 seconds released) toggles that button's corresponding relay, and holding it for 4 seconds triggers a factory reset. Each selected mode is saved independently and restored after reboot, subject to the existing 1-minute flash-write interval.

Select **Programmable** for a button to use it for Home Assistant automations. Switching modes leaves all relay states unchanged. In this mode that button does not directly control its relay; the existing **Light** or **LightN** entity still controls it independently. Modes can be mixed: for example, **Button1 Mode** can remain **Relay** while **Button2 Mode** is **Programmable**. Pressing Button1 then toggles relay 1, while Button2 reports events without toggling relay 2. Buttons recognize gestures independently, including when different buttons are operated at the same time.

Each button's event entity is enabled by default and reports these event types only while that button is in Programmable mode:

| Gesture | Event type | Timing |
| --- | --- | --- |
| Single click | `single_click` | Press for less than 1 second, then release for 300 ms without a second press. |
| Double click | `double_click` | Two presses of less than 1 second each, separated by less than 300 ms; reported after the final release has lasted 300 ms. No single-click event is emitted. |
| Long press | `long_press` | Reported once when the button has been held for 1 second. Releasing it does not emit a click. |

In Programmable mode, continuing to hold the button for **10 seconds** triggers a factory reset; the long-press event is still emitted at 1 second. A factory reset applies to the **entire device**, whether triggered by a Relay-mode button held for 4 seconds or a Programmable-mode button held for 10 seconds. The **Factory Reset** entity also remains available.

ESPHome event entities require **Home Assistant Core 2024.5 or newer**. The entity state is the timestamp of its latest event, and its `event_type` attribute identifies the gesture. Consecutive identical gestures update the timestamp each time. See the [ESPHome event documentation](https://esphome.io/components/event/) and [Home Assistant event documentation](https://www.home-assistant.io/integrations/event/).

On current Home Assistant releases, use the **Event received** trigger and select the desired event type. For example, this automation activates a scene on a double click of Button2 on a multi-gang switch. Replace the event entity ID and scene with your own; select the corresponding **Button Event** entity for a single-gang switch:

```yaml
automation:
  - alias: "Wall Switch Button2 double click"
    triggers:
      - trigger: event.received
        target:
          entity_id: event.your_switch_button2_event
        options:
          event_type:
            - double_click
    actions:
      - action: scene.turn_on
        target:
          entity_id: scene.your_scene
```

On older Home Assistant releases without the **Event received** trigger, trigger on the event entity's timestamp changing and inspect `event_type` in a condition. Triggering only on a change of the `event_type` attribute would miss consecutive identical gestures.

### RF433 IR Remote Pro: Sensor Firmware Variants

The RF433 IR Remote Pro ships with the standard firmware (`athom-rf-ir-remote-pro.yaml`). If you connect an external I2C sensor (SDA `GPIO5`, SCL `GPIO4`), switch to the matching firmware directly from Home Assistant:

1. Set **Firmware Variant** to **Standard**, **With sht40 sensor**, or **With scd40 sensor**. The selector always shows the variant currently running after a reboot.
2. Press **Install Selected Firmware**. The device downloads that variant's manifest from GitHub Pages and installs it over the air, then reboots.

All variants share the same device name and storage layout, so learned IR/RF signals and Home Assistant entities are kept. After switching, the **Firmware Update** entity follows the installed variant's manifest. If the manifest cannot be fetched within 60 seconds, the switch is aborted and logged.

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
