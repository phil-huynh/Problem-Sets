# **Making cupcakes**

# You and your friends have started a cupcake business to help you make money while you're working on your startup.

# You pooled your money and went to buy all the stuff needed for your gourmet cupcakes: flour, sugar, eggs, and tubes of frosting.

# But your calculations were off. After making all of the cupcakes you could with your ingredients, your group realizes that you don't have enough frosting for all of the cupcakes.

# You also find out two interesting facts:

# - People will buy your cupcakes with frosting for a certain amount of money.
# - People will buy your cupcakes without frosting for less money.
# - People will buy your unused tubes of frosting because there are people who just like eating the frosting.

# You and your friends decide to frost as many cupcakes as you can, then sell everything you've got: frosted cupcakes, cupcakes without frosting, and your leftover tubes of frosting.

# 5**Making cupcakes**Submitted on 10/07/2022
# Given the following input values:
# • `num_cupcakes`, which is how many cupcakes you have
# • `num_tubes_frosting`, which is how many tubes of frosting you have
# • `tubes_per_cupcake`, which is exactly how many tubes of frosting go on each cupcake

# Complete the function `profit` so that it returns the total dollars that you make given the following information:
# • A frosted cupcake sells for $10
# • A cupcake with no frosting sells for $4
# • A tube of frosting by itself sells for $1

# **Constraints**:
# • `10 <= num_cupcakes <= 100`
# • `10 <= num_tubes_frosting <= 50`
# • `1 <= tubes_per_cupcake <= 5`

# **Example**:
# Let's say you had 10 cupcakes, 5 tubes of frosting, and it takes 2 tubes of frosting to frost a cupcake. You can frost two cupcakes. You have one tube of frosting left over.ItemQuantitySelling priceTotalFrosted cupcake2$10$20Cupcake with no frosting8$4$32Leftover tubes of frosting1$1$1
# This means that you would make $53.


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