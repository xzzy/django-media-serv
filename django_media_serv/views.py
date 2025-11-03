from django.http import Http404, HttpResponse, JsonResponse, HttpResponseRedirect, StreamingHttpResponse
from django.conf import settings
import mimetypes
import os



def file_iterator(file_name, chunk_size=8192):
    with open(file_name, 'rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            yield chunk

def getMediaFile(request):
    file_path = request.path.replace("../","")

    extension = ""

    if request.path[-5:-4] == '.':
        extension = request.path[-4:]
    if request.path[-4:-3] == '.':
        extension = request.path[-3:]

    file_name_path = settings.BASE_DIR+file_path
    if os.path.isfile(file_name_path) is True:
              # the_file = open(file_name_path, 'rb')
              # the_data = the_file.read()
              # the_file.close()
              if extension == 'msg':
                  return StreamingHttpResponse(file_iterator(file_name_path), content_type="application/vnd.ms-outlook")
              if extension == 'eml':
                  return StreamingHttpResponse(file_iterator(file_name_path), content_type="application/vnd.ms-outlook")
              if extension == 'shp':
                  return StreamingHttpResponse(file_iterator(file_name_path), content_type="x-gis/x-shapefile")
              if extension == 'shx':
                  return StreamingHttpResponse(file_iterator(file_name_path), content_type="x-gis/x-shapefile")
              if extension == 'dbf':
                  return StreamingHttpResponse(file_iterator(file_name_path), content_type="text/plain")
              if extension == 'prj':
                  return StreamingHttpResponse(file_iterator(file_name_path), content_type="application/octet-stream")
              if extension == 'gpx':
                  return StreamingHttpResponse(file_iterator(file_name_path), content_type="application/gpx+xml")            
              if extension == 'docx':
                  return StreamingHttpResponse(file_iterator(file_name_path), content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document")                

              if len(extension) > 2:
                 return StreamingHttpResponse(file_iterator(file_name_path), content_type=mimetypes.types_map['.'+str(extension.lower())])
              else:
                 return HttpResponse("ERROR opening file", content_type="text/plain")
    else:
              return HttpResponse("ERROR opening file", content_type="text/plain")
#
