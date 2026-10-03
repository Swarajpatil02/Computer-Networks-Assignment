def classify_network_components(components):
    classification = {
        "Switch": (
            "Data Link Layer (Layer 2)",
            "Connects devices within a LAN and forwards frames using MAC addresses."
        ),
        "Router": (
            "Network Layer (Layer 3)",
            "Connects different networks and forwards packets using IP addresses."
        ),
        "Bridge": (
            "Data Link Layer (Layer 2)",
            "Connects LAN segments and filters/forwards frames using MAC addresses."
        ),
        "Access Point": (
            "Data Link Layer (Layer 2) / Physical Layer (Layer 1)",
            "Provides wireless network access and connects wireless devices to a wired LAN."
        ),
        "Twisted Pair Cable": (
            "Physical Layer (Layer 1)",
            "Carries electrical signals through copper wires."
        ),
        "Coaxial Cable": (
            "Physical Layer (Layer 1)",
            "Carries electrical signals through a shielded copper cable."
        ),
        "Fiber Optic Cable": (
            "Physical Layer (Layer 1)",
            "Transmits data using pulses of light through optical fiber."
        ),
        "Wireless/Radio": (
            "Physical Layer (Layer 1)",
            "Transmits data using electromagnetic radio waves."
        )
    }

    print("\nNETWORK COMPONENT CLASSIFICATION REPORT")
    print("=" * 90)
    print(f"{'Component':<25}{'Layer':<42}Primary Function")
    print("-" * 90)

    for component in components:
        if component in classification:
            layer, function = classification[component]
            print(f"{component:<25}{layer:<42}{function}")
        else:
            print(f"{component:<25}{'Not found':<42}No classification available.")

    print("=" * 90)


components = [
    "Switch",
    "Router",
    "Bridge",
    "Access Point",
    "Twisted Pair Cable",
    "Coaxial Cable",
    "Fiber Optic Cable",
    "Wireless/Radio"
]

classify_network_components(components)
