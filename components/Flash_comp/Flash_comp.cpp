#include "Flash_comp.h"

namespace esphome {
namespace flash_component {

void Flash_comp::setup() {
    nvs_flash_init();
}

bool Flash_comp::clear_signal_by_index(int index) {
    char key[12];
    sprintf(key, "irsig_%d", index);

    nvs_handle_t handle;
    if (nvs_open("storage", NVS_READWRITE, &handle) != ESP_OK) {
      ESP_LOGE("flash_comp", "Failed to open NVS handle");
      return false;
    }

    nvs_erase_key(handle, key);
    nvs_commit(handle);
    nvs_close(handle);
    return true;
}


}  // namespace flash_component
}  // namespace esphome
