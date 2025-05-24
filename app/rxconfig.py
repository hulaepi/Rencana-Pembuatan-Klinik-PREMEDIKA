import reflex as rx

config = rx.Config(
    app_name="app",
    tailwind={
        "theme": {
            "extend": {
                "colors": {
                    "tosca": {
                        "50": "#eff۹fa",
                        "100": "#d۱f۷f۵",
                        "200": "#a۷f۲ee",
                        "300": "#۷۲ede۵",
                        "400": "#۴۵e۳d۸",
                        "500": "#۲۲d۳c۴",
                        "600": "#۱۴b۱a۲",
                        "700": "#۱۲۹۳۸۵",
                        "800": "#۱۲۷۵۶c",
                        "900": "#۱۱۶۱۵۹",
                        "950": "#۰۵۳f۳a",
                    }
                },
                "fontFamily": {
                    "sans": ["Inter", "sans-serif"]
                },
            }
        },
        "plugins": [],
    },
)