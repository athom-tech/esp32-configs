import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor, uart
from esphome.const import (
    UNIT_PERCENT,
    CONF_ID,
)


DEPENDENCIES = ["uart"]
AUTO_LOAD = ["bl0906"]

bl0906_ns = cg.esphome_ns.namespace("bl0906")
BL0906 = bl0906_ns.class_(
    "BL0906", cg.PollingComponent, uart.UARTDevice
)

CONFIG_SCHEMA = (
    cv.Schema(
        {
            cv.GenerateID(): cv.declare_id(BL0906),
            cv.Optional("Frequency"): sensor.sensor_schema(
            accuracy_decimals = 0,
            device_class = "frequency",
            unit_of_measurement = "Hz"  
            ),
            cv.GenerateID(): cv.declare_id(BL0906),
            cv.Optional("Temperature"): sensor.sensor_schema(
            accuracy_decimals = 0,
            device_class = "temperature",
            unit_of_measurement = "℃"  
            ),
            cv.GenerateID(): cv.declare_id(BL0906),
            cv.Optional("Voltage"): sensor.sensor_schema(
            accuracy_decimals = 0,
            device_class = "voltage",
            unit_of_measurement = "V"  
            ),
            cv.Optional("Current_1"): sensor.sensor_schema(
            accuracy_decimals = 3,
            device_class = "current",
            unit_of_measurement = "A"  
            ),
            cv.Optional("Current_2"): sensor.sensor_schema(
            accuracy_decimals = 3,
            device_class = "current",
            unit_of_measurement = "A" 
            ),
            cv.Optional("Current_3"): sensor.sensor_schema(
            accuracy_decimals = 3,
            device_class = "current",
            unit_of_measurement = "A" 
            ),
            cv.Optional("Current_4"): sensor.sensor_schema(
            accuracy_decimals = 3,
            device_class = "current",
            unit_of_measurement = "A" 
            ),
            cv.Optional("Current_5"): sensor.sensor_schema(
            accuracy_decimals = 3,
            device_class = "current",
            unit_of_measurement = "A" 
            ),
            cv.Optional("Current_6"): sensor.sensor_schema(
            accuracy_decimals = 3,
            device_class = "current",
            unit_of_measurement = "A"  
            ),
            cv.Optional("Power_1"): sensor.sensor_schema(
            accuracy_decimals = 3,
            device_class = "power",
            unit_of_measurement = "W" 
            ),
            cv.Optional("Power_2"): sensor.sensor_schema(
            accuracy_decimals = 3,
            device_class = "power",
            unit_of_measurement = "W" 
            ),
            cv.Optional("Power_3"): sensor.sensor_schema(
            accuracy_decimals = 3,
            device_class = "power",
            unit_of_measurement = "W" 
            ),
            cv.Optional("Power_4"): sensor.sensor_schema(
            accuracy_decimals = 3,
            device_class = "power",
            unit_of_measurement = "W" 
            ),
            cv.Optional("Power_5"): sensor.sensor_schema(
            accuracy_decimals = 3,
            device_class = "power",
            unit_of_measurement = "W" 
            ),
            cv.Optional("Power_6"): sensor.sensor_schema(
            accuracy_decimals = 3,
            device_class = "power",
            unit_of_measurement = "W" 
            ),
            cv.Optional("Power_sum"): sensor.sensor_schema(
            accuracy_decimals = 3,
            device_class = "power",
            unit_of_measurement = "W" 
            ),
            cv.Optional("Energy_1"): sensor.sensor_schema(
            accuracy_decimals = 3,
            device_class = "energy",
            state_class = "total",  
            unit_of_measurement = "kWh" 
            ),
            cv.Optional("Energy_2"): sensor.sensor_schema(
            accuracy_decimals = 3,
            device_class = "energy",
            state_class = "total",
            unit_of_measurement = "kWh" ),
            cv.Optional("Energy_3"): sensor.sensor_schema(
            accuracy_decimals = 3,
            device_class = "energy",
            state_class = "total",
            unit_of_measurement = "kWh" 
            ),
            cv.Optional("Energy_4"): sensor.sensor_schema(
            accuracy_decimals = 3,
            device_class = "energy",
            state_class = "total",
            unit_of_measurement = "kWh" 
            ),
            cv.Optional("Energy_5"): sensor.sensor_schema(
            accuracy_decimals = 3,
            device_class = "energy",
            state_class = "total",
            unit_of_measurement = "kWh" 
            ),            
            cv.Optional("Energy_6"): sensor.sensor_schema(
            accuracy_decimals = 3,
            device_class = "energy",
            state_class = "total",
            unit_of_measurement = "kWh" 
            ),
            cv.Optional("Energy_sum"): sensor.sensor_schema(
            accuracy_decimals = 3,
            device_class = "energy",
            state_class = "total",
            unit_of_measurement = "kWh" 
            ),
        }
    )
    .extend(uart.UART_DEVICE_SCHEMA)
    .extend(cv.polling_component_schema("60s"))
)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await uart.register_uart_device(var, config)
    if "Frequency" in config:
        sens = await sensor.new_sensor(config["Frequency"])
        cg.add(var.set_frequency_sensor(sens))
    if "Temperature" in config:
        sens = await sensor.new_sensor(config["Temperature"])
        cg.add(var.set_temperature_sensor(sens))    
    if "Voltage" in config:
        sens = await sensor.new_sensor(config["Voltage"])
        cg.add(var.set_voltage_sensor(sens))
    if "Current_1" in config:
        sens = await sensor.new_sensor(config["Current_1"])
        cg.add(var.set_current_sensor_1(sens))  
    if "Current_2" in config:
        sens = await sensor.new_sensor(config["Current_2"])
        cg.add(var.set_current_sensor_2(sens))  
    if "Current_3" in config:
        sens = await sensor.new_sensor(config["Current_3"])
        cg.add(var.set_current_sensor_3(sens))  
    if "Current_4" in config:
        sens = await sensor.new_sensor(config["Current_4"])
        cg.add(var.set_current_sensor_4(sens))  
    if "Current_5" in config:
        sens = await sensor.new_sensor(config["Current_5"])
        cg.add(var.set_current_sensor_5(sens))  
    if "Current_6" in config:
        sens = await sensor.new_sensor(config["Current_6"])
        cg.add(var.set_current_sensor_6(sens))
    if "Power_1" in config:
        sens = await sensor.new_sensor(config["Power_1"])
        cg.add(var.set_power_sensor_1(sens))  
    if "Power_2" in config:
        sens = await sensor.new_sensor(config["Power_2"])
        cg.add(var.set_power_sensor_2(sens))  
    if "Power_3" in config:
        sens = await sensor.new_sensor(config["Power_3"])
        cg.add(var.set_power_sensor_3(sens))  
    if "Power_4" in config:
        sens = await sensor.new_sensor(config["Power_4"])
        cg.add(var.set_power_sensor_4(sens))  
    if "Power_5" in config:
        sens = await sensor.new_sensor(config["Power_5"])
        cg.add(var.set_power_sensor_5(sens))        
    if "Power_6" in config:
        sens = await sensor.new_sensor(config["Power_6"])
        cg.add(var.set_power_sensor_6(sens))  
    if "Power_sum" in config:
        sens = await sensor.new_sensor(config["Power_sum"])
        cg.add(var.set_power_sensor_sum(sens))           
    if "Energy_1" in config:
        sens = await sensor.new_sensor(config["Energy_1"])
        cg.add(var.set_energy_sensor_1(sens)) 
    if "Energy_2" in config:
        sens = await sensor.new_sensor(config["Energy_2"])
        cg.add(var.set_energy_sensor_2(sens)) 
    if "Energy_3" in config:
        sens = await sensor.new_sensor(config["Energy_3"])
        cg.add(var.set_energy_sensor_3(sens)) 
    if "Energy_4" in config:
        sens = await sensor.new_sensor(config["Energy_4"])
        cg.add(var.set_energy_sensor_4(sens)) 
    if "Energy_5" in config:
        sens = await sensor.new_sensor(config["Energy_5"])
        cg.add(var.set_energy_sensor_5(sens)) 
    if "Energy_6" in config:
        sens = await sensor.new_sensor(config["Energy_6"])
        cg.add(var.set_energy_sensor_6(sens))         
    if "Energy_sum" in config:
        sens = await sensor.new_sensor(config["Energy_sum"])
        cg.add(var.set_energy_sensor_sum(sens))   
     