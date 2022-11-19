def profit(num_cupcakes, num_tubes_frosting, tubes_per_cupcake):
    sale = 0
    for cupcake in range(num_cupcakes):
        if num_tubes_frosting >= tubes_per_cupcake:
            num_tubes_frosting -= tubes_per_cupcake
            num_cupcakes -= 1
            sale += 10
        else:
            num_cupcakes -= 1
            sale += 4
    sale += num_tubes_frosting
    return sale