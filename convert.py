import json

try:
    # 1. Open your huge 413-page file (make sure its filename matches exactly)
    with open('games.json', 'r', encoding='utf-8') as f:
        old_data = json.load(f)
    
    # 2. Setup the strict clean target framework SSPI requires
    sspi_structure = {"packages": []}
    
    # 3. Pull the main parent database block
    fpkgi_items = old_data.get("DATA", {})
    
    for url, details in fpkgi_items.items():
        name = details.get("name", "Unknown Game")
        version = details.get("version", "")
        region = details.get("region", "")
        
        # Build clean search attributes
        title_extra = f" ({region} - v{version})" if region or version else ""
        full_title = f"{name}{title_extra}"
        
        # Map old codes cleanly to uniform target tags
        package_block = {
            "title": full_title,
            "id": details.get("title_id", "CUSA00000"),
            "url": url,
            "icon": details.get("cover_url", "")
        }
        sspi_structure["packages"].append(package_block)
        
    # 4. Overwrite your old layout with 100% compatible SSPI syntax
    with open('games.json', 'w', encoding='utf-8') as f:
        json.dump(sspi_structure, f, indent=2)
        
    print("Success! Your 413 pages have been completely converted.")

except Exception as e:
    print(f"Error: {e}")
