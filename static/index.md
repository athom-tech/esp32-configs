# About

ESPhome project by Shenzhen Athom Technology Co., Ltd., China.

# Installation

Choose your device, then connect it over USB to install the matching pre-built firmware.

<section class="installer-panel" aria-label="Firmware installer">
  <div class="device-toolbar">
    <label class="device-field" for="device-select">
      <span>Device</span>
      <select id="device-select"></select>
    </label>
    <label class="device-field" for="device-search">
      <span>Search</span>
      <input id="device-search" type="search" placeholder="Filter devices" autocomplete="off">
    </label>
  </div>

  <div id="device-grid" class="device-grid" aria-label="Available devices"></div>

  <div class="install-row">
    <div>
      <h3 id="selected-device-title">Select a device</h3>
      <p id="selected-device-file">The installer will use the firmware manifest for the selected device.</p>
    </div>
    <esp-web-install-button id="install-button" manifest="firmware/Athom-ESP32-Device.manifest.json"></esp-web-install-button>
  </div>

  <p id="device-status" class="device-status" role="status"></p>
</section>

<style>
  .installer-panel {
    margin-top: 1.5rem;
  }

  .device-toolbar {
    display: grid;
    grid-template-columns: minmax(0, 1.2fr) minmax(180px, 0.8fr);
    gap: 14px;
    margin-bottom: 18px;
  }

  .device-field {
    display: grid;
    gap: 6px;
    color: #333;
    font-weight: 700;
  }

  .device-field select,
  .device-field input {
    box-sizing: border-box;
    width: 100%;
    min-height: 42px;
    border: 1px solid #c6cbd1;
    border-radius: 6px;
    padding: 8px 10px;
    background: #fff;
    color: #222;
    font: inherit;
  }

  .device-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
    gap: 10px;
    margin-bottom: 20px;
  }

  .device-option {
    min-height: 54px;
    border: 1px solid #d3d7dc;
    border-radius: 6px;
    padding: 10px 12px;
    background: #fff;
    color: #24292f;
    text-align: left;
    cursor: pointer;
    font: inherit;
  }

  .device-option:hover,
  .device-option:focus {
    border-color: #1e9fea;
    outline: none;
  }

  .device-option[aria-pressed="true"] {
    border-color: #1e9fea;
    box-shadow: inset 4px 0 0 #1e9fea;
  }

  .device-empty {
    grid-column: 1 / -1;
    margin: 0;
    color: #65717c;
  }

  .device-name {
    display: block;
    font-weight: 700;
    line-height: 1.25;
  }

  .device-yaml {
    display: block;
    margin-top: 4px;
    color: #65717c;
    font-size: 0.82rem;
    line-height: 1.2;
    overflow-wrap: anywhere;
  }

  .install-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 20px;
    border-top: 1px solid #d8dde3;
    padding-top: 18px;
  }

  .install-row h3 {
    margin: 0 0 4px;
    color: #24292f;
  }

  .install-row p,
  .device-status {
    margin: 0;
    color: #4d5660;
  }

  .device-status {
    margin-top: 12px;
    min-height: 1.4em;
  }

  @media (max-width: 700px) {
    .device-toolbar {
      grid-template-columns: 1fr;
    }

    .install-row {
      align-items: flex-start;
      flex-direction: column;
    }
  }
</style>

<script type="module" src="https://unpkg.com/esp-web-tools@10/dist/web/install-button.js?module"></script>
<script>
  const fallbackDevices = [
    "athom-1gang-switch",
    "athom-2ch-relay-board",
    "athom-2gang-switch",
    "athom-3gang-switch",
    "athom-4ch-relay-board",
    "athom-4gang-switch",
    "athom-8ch-relay-board",
    "athom-energy-monitor-x2",
    "athom-energy-monitor-x6",
    "athom-garage-door",
    "athom-ld2450-sensor",
    "athom-mini-relay-v2",
    "athom-presence-sensor-v3",
    "athom-rf-ir-remote",
    "athom-rgbcw-bulb",
    "athom-rgbcw-light",
    "athom-scd40-sensor",
    "athom-sht40-sensor",
    "athom-smart-plug",
    "athom-smart-plug-v5",
    "athom-wall-outlet-v3",
    "athom-zigbee-gateway"
  ].map((id) => ({
    id,
    name: formatDeviceName(id),
    yaml: `${id}.yaml`,
    manifest: `firmware/${id}.manifest.json`
  }));

  const state = {
    devices: [],
    selectedId: "",
    filter: ""
  };

  const select = document.querySelector("#device-select");
  const search = document.querySelector("#device-search");
  const grid = document.querySelector("#device-grid");
  const installButton = document.querySelector("#install-button");
  const title = document.querySelector("#selected-device-title");
  const file = document.querySelector("#selected-device-file");
  const status = document.querySelector("#device-status");

  function formatDeviceName(id) {
    return id
      .split("-")
      .map((part) => part.charAt(0).toUpperCase() + part.slice(1))
      .join(" ");
  }

  function normalizeDevice(device) {
    return {
      id: device.id,
      name: device.name || formatDeviceName(device.id),
      yaml: device.yaml || `${device.id}.yaml`,
      manifest: device.manifest || `firmware/${device.id}.manifest.json`
    };
  }

  async function loadDevices() {
    try {
      const response = await fetch("firmware/devices.json", { cache: "no-store" });
      if (!response.ok) {
        throw new Error(`devices.json returned ${response.status}`);
      }
      const data = await response.json();
      state.devices = data.devices.map(normalizeDevice);
      status.textContent = `Firmware index loaded for ESPHome ${data.version}.`;
    } catch (error) {
      state.devices = fallbackDevices;
      status.textContent = "Firmware index is not available yet; using the built-in device list.";
    }

    state.selectedId = state.devices[0]?.id || "";
    render();
  }

  function getSelectedDevice() {
    return state.devices.find((device) => device.id === state.selectedId) || state.devices[0];
  }

  function getVisibleDevices() {
    const query = state.filter.trim().toLowerCase();
    if (!query) {
      return state.devices;
    }

    return state.devices.filter((device) =>
      `${device.name} ${device.id} ${device.yaml}`.toLowerCase().includes(query)
    );
  }

  function selectDevice(id) {
    state.selectedId = id;
    render();
  }

  function renderSelect() {
    select.replaceChildren();
    for (const device of state.devices) {
      const option = document.createElement("option");
      option.value = device.id;
      option.textContent = device.name;
      option.selected = device.id === state.selectedId;
      select.append(option);
    }
  }

  function renderGrid() {
    grid.replaceChildren();
    const visibleDevices = getVisibleDevices();

    if (visibleDevices.length === 0) {
      const empty = document.createElement("p");
      empty.className = "device-empty";
      empty.textContent = "No matching devices.";
      grid.append(empty);
      return;
    }

    for (const device of visibleDevices) {
      const button = document.createElement("button");
      button.type = "button";
      button.className = "device-option";
      button.setAttribute("aria-pressed", String(device.id === state.selectedId));
      button.dataset.deviceId = device.id;
      button.innerHTML = `
        <span class="device-name"></span>
        <span class="device-yaml"></span>
      `;
      button.querySelector(".device-name").textContent = device.name;
      button.querySelector(".device-yaml").textContent = device.yaml;
      button.addEventListener("click", () => selectDevice(device.id));
      grid.append(button);
    }
  }

  function renderInstaller() {
    const device = getSelectedDevice();
    if (!device) {
      title.textContent = "No devices found";
      file.textContent = "";
      installButton.setAttribute("manifest", "firmware/Athom-ESP32-Device.manifest.json");
      return;
    }

    title.textContent = device.name;
    file.textContent = `${device.yaml} -> ${device.manifest}`;
    installButton.setAttribute("manifest", device.manifest);
  }

  function render() {
    renderSelect();
    select.value = state.selectedId;
    renderGrid();
    renderInstaller();
  }

  select.addEventListener("change", (event) => selectDevice(event.target.value));
  search.addEventListener("input", (event) => {
    state.filter = event.target.value;
    renderGrid();
  });

  loadDevices();
</script>
