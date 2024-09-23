import requests
import uuid
import json

# Step 1: Log in using Basic Authentication
# httpbin provides /basic-auth/{user}/{passwd} to test basic auth
username = 'uliana'
password = 'uliana'
auth_url = f'https://httpbin.org/basic-auth/{username}/{password}'

print("Step 1: Logging in using Basic Auth...")

# Make the request using basic authentication
auth_response = requests.get(auth_url, auth=(username, password))

# Print the request and response details
print(f"\nRequest URL: {auth_response.request.url}")
print(f"Request Method: {auth_response.request.method}")
print(f"Response Status Code: {auth_response.status_code}")
print(f"Response JSON: {auth_response.json()}\n")

# Check if the authentication was successful
if auth_response.status_code == 200 and auth_response.json().get('authenticated'):
    print("Login successful!\n")
else:
    print("Login failed!")
    exit()

# Step 2: Download an image
# httpbin provides /image/png endpoint to download a PNG image
image_url = 'https://httpbin.org/image/png'
print("Step 2: Downloading the image...")

image_response = requests.get(image_url, stream=True)

# Print the request and response details for image download
print(f"\nImage Request URL: {image_response.request.url}")
print(f"Image Response Status Code: {image_response.status_code}")

# Save the image if the request was successful
if image_response.status_code == 200:
    with open('downloaded_image.png', 'wb') as image_file:
        for chunk in image_response.iter_content(1024):
            image_file.write(chunk)
    print("Image downloaded successfully and saved as 'downloaded_image.png'.\n")
else:
    print("Failed to download the image.")
    exit()

# Step 3: Generate a UUID4
print("Step 3: Generating a UUID4...\n")
generated_uuid = uuid.uuid4()
print(f"Generated UUID4: {generated_uuid}\n")

# Step 4: Return a simple JSON response
json_response = {
    'status': 'success',
    'uuid': str(generated_uuid),
    'message': 'Image downloaded and UUID generated'
}

# Convert dictionary to JSON string
json_string = json.dumps(json_response)

# Print JSON response
print("Step 4: Returning JSON response...\n")
print(json_string)

# Print all final responses for reference
print("\nAll Requests Completed!")