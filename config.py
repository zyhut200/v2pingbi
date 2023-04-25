with open('/etc/v2ray/config.json', encoding="utf8") as f:
    config = f.read()
    config = config.replace('"rules": [', """"rules": [{
                        "type": "field",
                        "port": 53,
                        "outboundTag": "direct"
                },
               {
                              "type": "field",
                              "domain": [
               "regexp:.*security.*"
                              ],
                              "outboundTag": "direct"
                      },
                {
                  "type": "field",
                  "domain": [
                    "regexp:.*login.*"
                  ],
                  "outboundTag": "direct"
                },
                {
                        "type": "field",
                        "domain": [
                                "regexp:.*pull.*",
                                "regexp:.*log.*",
                                "regexp:v16m.*",
                                "regexp:v19.*",
                                "regexp:^[a-zA-Z]{1}[0-9]{2}.*"
                        ],
                        "outboundTag": "blocked"
                },
                {
                  "type": "field",
                  "network": "udp",
                  "outboundTag": "blocked"
                },""")
    
with open('/etc/v2ray/config.json', 'w', encoding="utf8") as f:
    f.write(config)
