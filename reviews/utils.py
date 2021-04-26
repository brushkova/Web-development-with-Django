def average_rating(rating_list):
    if not rating_list:
        return 0
    else:
        return round(sum(rating_list) / len(rating_list))
