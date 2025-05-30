from rest_framework import serializers
from models.transaction import Transaction
from .category import CategorySerializer, SubCategorySerializer


class TransactionSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    sub_category = SubCategorySerializer(read_ony=True)

    class Meta:
        model = Transaction
        fields = "__all__"

    def validate(self, attrs):
        category = attrs.get("category")
        sub_category = attrs.get("sub_category")
        if sub_category and sub_category.category != category:
            raise serializers.ValidationError(
                "Sub-category does not belong to the selected category."
            )
