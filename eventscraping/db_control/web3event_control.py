from eventAPI.models import Web3event
import json
import requests
import tempfile
from django.core import files

def create_event(event_detail):
    title = event_detail['title'] if "title" in event_detail else ""
    description = event_detail['description'] if "description" in event_detail else ""
    time = event_detail['time'] if "time" in event_detail else ""
    address = event_detail['addr'] if "addr" in event_detail else ""
    organizers = json.dumps(event_detail['organizers']) if "organizers" in event_detail else ""
    presenter = ', '.join(event_detail['presenter']) if "presenter" in event_detail else ""
    tags = ', '.join(event_detail['tags']) if "tags" in event_detail else ""

    web3_event = Web3event.objects.create(title=title, time=time, address=address, organizers=organizers, presenter=presenter, tags=tags, description=description)
    image_url = event_detail['image'] if "image" in event_detail else ""

    # download_image_from_url(image_url)
    if image_url:
         # Stream the image from the url
        response = requests.get(image_url, stream=True)  
                  
        # Get the filename from the url, used for saving later
        file_name = image_url.split('/')[-1]
        
        # Create a temporary file
        lf = tempfile.NamedTemporaryFile()

        # Read the streamed image in sections
        for block in response.iter_content(1024 * 8):
            
            # If no more file then stop
            if not block:
                break

            # Write image block to temporary file
            lf.write(block)
        web3_event.image.save(file_name, files.File(lf))