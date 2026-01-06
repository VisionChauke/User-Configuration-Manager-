# Step 1: Create a dictionary to store user configuration preferences
test_settings = {
    'theme': 'light',
    'notifications': 'enabled'
}

# Step 2: Define add_setting function
def add_setting(settings, kv_pair):
    key, value = kv_pair
    key = key.lower()
    value = value.lower()
    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"

# Step 3: Define update_setting function
def update_setting(settings, kv_pair):
    key, value = kv_pair
    key = key.lower()
    value = value.lower()
    if key in settings:
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

# Step 4: Define delete_setting function
def delete_setting(settings, key):
    key = key.lower()
    if key in settings:
        del settings[key]
        return f"Setting '{key}' deleted successfully!"
    return "Setting not found!"

# Step 5: Define view_settings function
def view_settings(settings):
    if not settings:
        return "No settings available."
    
    result = "Current User Settings:\n"
    for key, value in settings.items():
        result += f"{key.capitalize()}: {value}\n"
    return result
