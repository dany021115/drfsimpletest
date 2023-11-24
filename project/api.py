from .models import Projects
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view
from .serializers import ProjectSerializers
from rest_framework.response import Response


class ProjectViewsSet(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializers


@api_view(['DELETE'])
def del_api(request, id):
    try:
        pjt = Projects.objects.get(pk=id)
        pjt.delete()
        return Response({
            "detalle": "Eliminado"
        })
    except:  
        return Response({
            "detalle": "id no existe"
        })
