#pragma once

#include "esphome.h"
#include "esphome/core/component.h"
#include <vector>
#include <nvs_flash.h>

namespace esphome {
namespace flash_component {

class Flash_comp : public Component {
public:

  void setup() override;

  template<typename T>
  bool save_to_nvs(int index, const std::vector<T> data){
      char key[12];
      sprintf(key, "irsig_%d", index);

      nvs_handle_t handle;
      if (nvs_open("storage", NVS_READWRITE, &handle) != ESP_OK) {
        ESP_LOGE("flash_comp", "Failed to open NVS handle");
        return false;
      }

      // delete old data
      nvs_erase_key(handle, key);

      // store new data
      if (data.size() > 0) {
        esp_err_t err = nvs_set_blob(handle, key, data.data(), data.size() * sizeof(long int));
        if (err != ESP_OK) {
          ESP_LOGE("flash_comp", "Failed to write data: %d", err);
          return false;
        }
      }
      ESP_LOGI("flash_comp", "Saved %d data to NVS", data.size());
      // commit changes
      nvs_commit(handle);
      nvs_close(handle);
      return true;
  }

  template<typename T>
  std::vector<T> load_from_nvs(int index) {
    char key[12];
    sprintf(key, "irsig_%d", index);
    std::vector<T> data;

    nvs_handle_t handle;
    if (nvs_open("storage", NVS_READONLY, &handle) != ESP_OK) {
      ESP_LOGE("flash_comp", "Failed to open NVS handle");
      return data;
    }

    // get data size
    size_t required_size = 0;
    esp_err_t err = nvs_get_blob(handle, key, nullptr, &required_size);

    if (err == ESP_OK && required_size > 0) {
      // add data to vector
      data.resize(required_size / sizeof(long int));
      nvs_get_blob(handle, key, data.data(), &required_size);
    } else if (err != ESP_ERR_NVS_NOT_FOUND) {
      ESP_LOGE("flash_comp", "Failed to read data: %d", err);
    }
    ESP_LOGI("flash_comp", "Loaded %d data from NVS", data.size());
    nvs_close(handle);
    return data;
  }

  bool clear_signal_by_index(int index);
};

}  // namespace flash_component
}  // namespace esphome
