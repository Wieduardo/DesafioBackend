from rest_framework import serializers
import ipdb

from .models import CNABdoc, CNABfile

class CNABdocSerializer(serializers.ModelSerializer):
    
    class Meta:

        model = CNABfile

        fields = [
            "cnab_doc"
        ]
        

    def create(self, validated_data):

        CNAB_file_object= CNABfile.objects.create(**validated_data)

        path= validated_data['cnab_doc'].name

        conteudo = open(f'cnabdoc/{path}', 'r', encoding="utf-8")

        conteudo_formatado = conteudo.read()

        parts = [conteudo_formatado[i:i+80] for i in range(0, len(conteudo_formatado), 81)]

        for part in parts:
            part1=part[0:1]
            part2=part[1:9]
            part3=part[9:19]
            part4=part[19:30]
            part5=part[30:42]
            part6=part[42:48]
            part7=part[48:62]
            part8=part[62:81]

            CNAB_object = CNABdoc.objects.create(
                type=part1,
                date=f'{part2[0:4]}-{part2[5:6]}-{part2[7:8]}',
                value=int(part3)/100,
                cpf=part4,
                card=part5,
                hour=f'{part6[0:2]}:{part6[3:4]}:{part6[5:6]}',
                owner=part7,
                store=part8
            )

        conteudo.close()

        return CNAB_file_object

class CNABentriesSerializer(serializers.ModelSerializer):

    class Meta:

        model = CNABdoc

        fields = [
            "id",
            "type",
            "date",
            "value",
            "cpf",
            "card",
            "hour",
            "owner",
            "store"
        ]

        ready_only_fields = ["id"]

