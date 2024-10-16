from faker import Faker
import csv
import random

# Initialize Faker
fake = Faker()

# Enter the number of users to generate
number_of_users = 35
users = []

# List of departments, cities, states & jobs
departments = ["RH", "IT", "Compliance", "Audit", "Finance", "Marketing", "Ventes", "Support Client"]
cities = ["Douala", "Yaoundé", "Bafoussam", "Kribi", "Garoua", "Abidjan", "Libreville", "Malabo", "Dakar", "Limbe"]
states = ["Littoral", "Centre", "Ouest", "Sud", "Nord"]
countries = ["Cameroon", "Guinea", "Ivory Coast", "Senegal", "Gabon"]
job_titles = {
    "RH": ["Responsable RH", "Assistant RH", "Recruteur"],
    "IT": ["Développeur", "Administrateur Système", "Analyste Sécurité"],
    "Compliance": ["Responsable Conformité", "Analyste Conformité"],
    "Audit": ["Auditeur Interne", "Responsable Audit"],
    "Finance": ["Analyste Financier", "Comptable", "Contrôleur de Gestion"],
    "Marketing": ["Responsable Marketing", "Spécialiste SEO", "Community Manager"],
    "Ventes": ["Commercial", "Responsable Ventes", "Assistant Commercial"],
    "Support Client": ["Technicien Support", "Responsable Support", "Agent Support"]
}

# Generate the users
for _ in range(number_of_users):
    department = random.choice(departments)
    city = random.choice(cities)
    state = random.choice(states)
    job_title = random.choice(job_titles[department])
    first_name = fake.first_name()
    last_name = fake.last_name()
    display_name = f"{first_name} {last_name}"
    user_principal_name = f"{first_name.lower()}.{last_name.lower()}@likabo-ind.me"
    country = random.choice(countries)
    
    user = {
        "Nom [displayName] Obligatoire": display_name,
        "Nom d'utilisateur [userPrincipalName] Obligatoire": user_principal_name,
        "Mot de passe initial [passwordProfile] Obligatoire": fake.password(),
        "Bloquer la connexion (Oui/Non) [accountEnabled] Obligatoire": "Non",
        "Prénom [givenName]": first_name,
        "Nom de famille [surname]": last_name,
        "Poste [jobTitle]": job_title,
        "Service [department]": department,
        "Lieu d'utilisation [usageLocation]": fake.country_code(),
        "Rue [streetAddress]": fake.street_address(),
        "Département ou région [state]": state,
        "Pays ou région [country]": country,
        "Office [physicalDeliveryOfficeName]": fake.company(),
        "Ville [city]": city,
        "Code postal [postalCode]": fake.postcode(),
        "Téléphone (bureau) [telephoneNumber]": fake.phone_number(),
        "Téléphone mobile [mobile]": fake.phone_number()
    }
    users.append(user)

# Save the users in a csv file
with open('users.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    
    # first line of the csv file following Azure template
    writer.writerow(['version:v1.0'])
    
    # first columns of the csv file following Azure template
    fieldnames = [
        "Nom [displayName] Obligatoire", "Nom d'utilisateur [userPrincipalName] Obligatoire", "Mot de passe initial [passwordProfile] Obligatoire", "Bloquer la connexion (Oui/Non) [accountEnabled] Obligatoire",
        "Prénom [givenName]", "Nom de famille [surname]", "Poste [jobTitle]", "Service [department]", "Lieu d'utilisation [usageLocation]", "Rue [streetAddress]",
        "Département ou région [state]", "Pays ou région [country]", "Office [physicalDeliveryOfficeName]", "Ville [city]", "Code postal [postalCode]",
        "Téléphone (bureau) [telephoneNumber]", "Téléphone mobile [mobile]"
    ]

    writer.writerow(fieldnames)
    
    # Write the users information
    for user in users:
        writer.writerow([user[field] for field in fieldnames])

print('Utilisateurs générés et sauvegardés dans users.csv')