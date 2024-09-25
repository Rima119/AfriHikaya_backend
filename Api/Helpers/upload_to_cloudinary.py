import cloudinary.uploader

def upload(file, folder, resource_type, public_id):
    upload_result = cloudinary.uploader.upload(file, resource_type=resource_type, folder=folder, public_id=public_id)
    return upload_result['url']
