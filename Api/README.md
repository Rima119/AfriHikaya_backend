## To upload image to Cloudinary use this line of code
upload_result = cloudinary.uploader.upload(imageFile, resource_type = "image", folder="cloudinary_folder_name_here", public_id="file_name")
image_url = upload_result['url']