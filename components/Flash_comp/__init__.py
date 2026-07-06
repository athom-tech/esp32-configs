import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.const import CONF_ID

flash_comp_ns = cg.esphome_ns.namespace('flash_component')
Flash_comp = flash_comp_ns.class_('Flash_comp', cg.Component)

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(Flash_comp),
}).extend(cv.COMPONENT_SCHEMA)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
