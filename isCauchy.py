import math

def is_cauchy_sequence(epsilon=1e-6, max_iterations=1000):
    # Fonction pour calculer le terme de la suite
    def sequence_term(n):
        return sum(math.sin(k) / (2 ** k) for k in range(n + 1))

    # Initialisation des variables
    n = 0
    m = 0
    delta = float('inf')  # Initialisation de delta à une valeur infinie

    # Boucle pour calculer les termes de la suite et vérifier la condition de Cauchy
    while delta > epsilon and n < max_iterations:
        m = n  # On commence par prendre m = n
        V_m = sequence_term(m)  # Calcul de V_m
        n += 1
        V_n = sequence_term(n)  # Calcul de V_n

        # Calcul de la différence |V_n - V_m|
        delta = abs(V_n - V_m)

        # Affichage des valeurs pour suivre l'évolution
        print(f"n = {n}, V_n = {V_n}, delta = {delta}")

    # Vérification de la condition de Cauchy
    if delta <= epsilon:
        print(f"La suite est de Cauchy pour epsilon = {epsilon} après {n} itérations.")
    else:
        print(f"La suite n'est pas de Cauchy après {max_iterations} itérations avec epsilon = {epsilon}.")

# Exécution de la fonction avec une précision de 1e-6
is_cauchy_sequence()