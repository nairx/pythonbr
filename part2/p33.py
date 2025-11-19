result = {
    "Maths":57,
    "English":90,
    "Science":50
}
print(max(result,key=result.get))
print(min(result,key=result.get))