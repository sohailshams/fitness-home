from django.shortcuts import get_object_or_404
from merchandise.models import Product
from exercise.models import ExercisePlans
from nutrition.models import NutritionPlans


def cart_contents(request):
    cart_items = {
        'merchandise_items': [],
        'exercise_items': [],
        'nutrition_items': [],
        }

    total_merchandise = 0
    total_exercise = 0
    total_nutrition = 0
    total = 0
    product_count = 0
    exercise_count = 0
    nutrition_count = 0
    total_item_count = 0

    cart = request.session.get('cart', {
        'merchandise_dic': {},
        'excercise_plans_dic': {},
        'nutrition_plans_dic': {},
    })
    for product_type, dic in cart.items():
        if product_type == 'merchandise_dic':
            for item_id, quantity in dic.items():
                product = get_object_or_404(Product, pk=item_id)
                total_merchandise += quantity * product.price
                product_count += quantity
                cart_items['merchandise_items'].append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    })
        elif product_type == 'nutrition_plans_dic':
            for item_id, quantity in dic.items():
                nutrition = get_object_or_404(NutritionPlans, pk=item_id)
                total_nutrition += quantity * nutrition.price
                nutrition_count += quantity
                cart_items['nutrition_items'].append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'nutrition': nutrition,
                    })
        else:
            for item_id, quantity in dic.items():
                exercise = get_object_or_404(ExercisePlans, pk=item_id)
                total_exercise += quantity * exercise.price
                exercise_count += quantity
                cart_items['exercise_items'].append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'exercise': exercise,
                    })

    total = total_merchandise + total_exercise + total_nutrition
    total_item_count = product_count + exercise_count + nutrition_count
    context = {
        'cart_items': cart_items,
        'total': total,
        'total_item_count': total_item_count
    }

    return context
