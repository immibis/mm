# Follows the format of Address:(Name, Type, Array Info)
{
    # NOTE These symbols could be one of two symbols: the start of a file or the end of a file before it.
    #      The choice for disassembly is arbitrary but in code it should be the one that makes sense.
    0x0001A500:("dmadata_vrom_start","u32",""), # Start of dmadata
    0x00020700:("dmadata_vrom_end","u32",""), # Byte immediately after end of dmadata
    0x00046AF0:("Audioseq_vrom_start","UNK_TYPE",""),
    0x00097F70:("Audioseq_vrom_end","UNK_TYPE",""),
    0x0065D000:("link_animetion_vrom_start","UNK_TYPE",""),
    0x00957000:("","UNK_TYPE",""), # ovl_kaleido_scope uses this. It is the start of vrom for a null entry in dmadata???
    0x009ECEC0:("","UNK_TYPE",""), # ovl_kaleido_scope uses this. It is the end of vrom for a null entry in dmadata???
    0x009ED000:("","UNK_TYPE",""), # ovl_kaleido_scope uses this. It is the start of vrom for a null entry in dmadata???
    0x009F4700:("","UNK_TYPE",""), # ovl_kaleido_scope uses this. It is the end of vrom for a null entry in dmadata???
    0x009F5000:("icon_item_field_static_vrom_start","UNK_TYPE",""),
    0x00A09AF0:("icon_item_field_static_vrom_end","UNK_TYPE",""),
    0x00A0A000:("icon_item_dungeon_static_vrom_start","UNK_TYPE",""),
    0x00A0EB80:("icon_item_dungeon_static_vrom_end","UNK_TYPE",""),
    0x00A0F000:("icon_item_gameover_static_vrom_start","UNK_TYPE",""),
    0x00A12300:("icon_item_gameover_static_vrom_end","UNK_TYPE",""),
    0x00A13000:("_013_0x00963540_vrom_start","UNK_TYPE",""),
    0x00A1BA00:("_013_0x00963540_vrom_end","UNK_TYPE",""),
    0x00A1C000:("_014_0x00967260_vrom_start","UNK_TYPE",""),
    0x00A1C2E0:("_014_0x00967260_vrom_end","UNK_TYPE",""),
    0x00A1D000:("map_i_static_vrom_start","UNK_TYPE",""),
    0x00A1E310:("map_grand_static_vrom_start","UNK_TYPE",""),
    0x00A27660:("item_name_static_vrom_start","UNK_TYPE",""),
    0x00A352F0:("map_name_static_vrom_start","UNK_TYPE",""),
    0x00A36C10:("_019_0x00980f60_vrom_start","UNK_TYPE",""),
    0x00A7BEE0:("_020_0x009c6230_vrom_start","UNK_TYPE",""),
    0x00A807A0:("_020_0x009c6230_vrom_end","UNK_TYPE",""),
    0x00A8C000:("_022_0x009caaf0_vrom_start","UNK_TYPE",""),
    0x00A92A10:("_023_0x009d1500_vrom_start","UNK_TYPE",""),
    0x00A990E0:("_023_0x009d1500_vrom_end","UNK_TYPE",""),
    0x00A9A000:("_024_0x009d3760_vrom_start","UNK_TYPE",""),
    0x00ABFC00:("_024_0x009d3760_vrom_end","UNK_TYPE",""),
    0x00AC0000:("do_action_static_vrom_start","UNK_TYPE",""),
    0x00AC4000:("message_static_vrom_start","UNK_TYPE",""),
    0x00ACA000:("message_texture_static_vrom_start","UNK_TYPE",""),
    0x00ACC000:("nes_font_static_vrom_start","UNK_TYPE",""),
    0x00AD1000:("en_message_data_static_vrom_start","UNK_TYPE",""),
    0x00B3B000:("staff_message_data_static_vrom_start","UNK_TYPE",""),
    0x00B3C000:("code_vrom_start","UNK_TYPE",""),
    0x00C7A4E0:("code_vrom_end","UNK_TYPE",""),
    0x01E85000:("nintendo_rogo_static_vrom_start","UNK_TYPE",""),
    0x01E87DC0:("nintendo_rogo_static_vrom_end","UNK_TYPE",""),
    0x01E88000:("title_static_vrom_start","UNK_TYPE",""),
    0x01EB9730:("title_static_vrom_end","UNK_TYPE",""),
    0x01EBA000:("_1124_0x0163f490_vrom_start","UNK_TYPE",""),
    0x01EBB280:("_1124_0x0163f490_vrom_end","UNK_TYPE",""),
    0x01EBC000:("_1125_0x0163fc10_vrom_start","UNK_TYPE",""),
    0x01EBC680:("_1125_0x0163fc10_vrom_end","UNK_TYPE",""),
    0x01EBD000:("_1126_0x0163ffc0_vrom_start","UNK_TYPE",""),
    0x01EC8B20:("_1126_0x0163ffc0_vrom_end","UNK_TYPE",""),
    0x01EC9000:("_1127_0x01643d50_vrom_start","UNK_TYPE",""),
    0x01EC9F30:("_1127_0x01643d50_vrom_end","UNK_TYPE",""),
    0x01ECA000:("_1128_0x01644c80_vrom_start","UNK_TYPE",""),
    0x01ED3B00:("_1128_0x01644c80_vrom_end","UNK_TYPE",""),
    0x01ED4000:("_1129_0x01646b60_vrom_start","UNK_TYPE",""),
    0x01EDDB00:("_1129_0x01646b60_vrom_end","UNK_TYPE",""),
    0x01EDE000:("_1130_0x01649020_vrom_start","UNK_TYPE",""),
    0x01EE7B00:("_1130_0x01649020_vrom_end","UNK_TYPE",""),
    0x01EE8000:("_1131_0x0164ad90_vrom_start","UNK_TYPE",""),
    0x01EF1B00:("_1131_0x0164ad90_vrom_end","UNK_TYPE",""),
    0x01EF2000:("vr_fine_static_vrom_start","UNK_TYPE",""),
    0x01EFE000:("vr_cloud_static_vrom_start","UNK_TYPE",""),
    0x01F0A000:("vr_pal_static_vrom_start","UNK_TYPE",""),
    0x01F0A200:("vr_pal_static_vrom_end","UNK_TYPE",""),
}