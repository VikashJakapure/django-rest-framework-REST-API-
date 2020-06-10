Simple Django rest app demonstration how to upload file using API

----------------------------------------------------------------------------------------------------------------------

Use MultipartParser from rest_framework.parsers import MultiPartParser as below :-


class FileHandleView(APIView):

    parser_classes = [MultiPartParser]

    def put(self,request):
        file_obj = request.data['file']
        # print(file_obj.read())
        data = file_obj.read()
        with open('temp_'+file_obj.name,'wb') as file:
            file.write(data)

        return Response("Success")


----------------------------------------------------------------------------------------------------------------------

curl API request :-

curl -X PUT -H "Content-Type: multipart/form-data"  -F "file=@test.txt" http://127.0.0.1:8000/api/upload/
 
----------------------------------------------------------------------------------------------------------------------

reference :-  https://www.django-rest-framework.org/api-guide/parsers/
