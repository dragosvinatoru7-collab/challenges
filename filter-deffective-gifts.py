def filter_gifts(gifts):
  # Code here
  non_deffective_gifts = []
  for gift in gifts:
    is_deffect = gift.contains('#')
    if not is_deffect:
      non_deffective_gifts.append(gift)
  return non_deffective_gifts
