users = {
    'jperez': {'password':'1234','rol':'alumno', 'nombre': 'Juan Peréz'},
    'amartin': {'password':'1234','rol':'alumno','nombre': 'Ana Martin'},
    'mvilchis':{'password':'1234','rol':'alumno','nombre': 'Melany Vilchis'},
    'ryerbes':{'password':'1234','rol':'alumno','nombre': 'Roberto Yerbes'},
    'rfarah':{'password':'1234','rol':'alumno','nombre': 'Rafita Farah'},
    'vnoh':{'password':'1234','rol':'alumno','nombre':'Venus Noh'},
    'jpedrozo':{'password':'1234','rol':'maestro','nombre': 'Javier Pedrozo'},
    'dgamboa':{'password':'1234','rol':'coordinador','nombre':'Didier Gamboa'},
}

# Se mantienen tus materias personalizadas
subjects = (
    "Discrete Mathematics", "Programming", "English II", 
    "Differential Calculus", "Probability and Statistics", 
    "Computer and Server Architecture", "Socio-Emotional Skills and Conflict Management"
)

notes = {
    'jperez': {'Discrete Mathematics': 8.5,'Programming': 9.2,'English II': 9.0, 'Differential Calculus': 7.8,'Probability and Statistics': 8.3,'Computer and Server Architecture': 6.8,'Socio-Emotional Skills and Conflict Management': 9.5},
    'amartin': {'Discrete Mathematics': 9.0,'Programming': 6.7,'English II': 9.4,'Differential Calculus': 6.2,'Probability and Statistics': 9.1,'Computer and Server Architecture': 6.5, 'Socio-Emotional Skills and Conflict Management': 9.8},
    'mvilchis': {'Discrete Mathematics': 7.5,'Programming': 8.0,'English II': 8.5,'Differential Calculus': 7.0,'Probability and Statistics': 7.8,'Computer and Server Architecture': 6.2,'Socio-Emotional Skills and Conflict Management': 8.9},
    'ryerbes': {'Discrete Mathematics': 9.5,'Programming': 9.8,'English II': 9.2,'Differential Calculus': 9.0,'Probability and Statistics': 9.6,'Computer and Server Architecture': 9.4,'Socio-Emotional Skills and Conflict Management': 10.0},
    'rfarah': {'Discrete Mathematics': 8.2,'Programming': 6.9,'English II': 8.8,'Differential Calculus': 6.0,'Probability and Statistics': 6.4,'Computer and Server Architecture': 8.1,'Socio-Emotional Skills and Conflict Management': 9.0},
    'vnoh': {'Discrete Mathematics': 8.8,'Programming': 9.0,'English II': 8.5,'Differential Calculus': 6.6,'Probability and Statistics': 8.9,'Computer and Server Architecture': 8.7,'Socio-Emotional Skills and Conflict Management': 9.2},
}

# PROCESS - LOGIN
while True:
    user = input("User: ")
    password = input("Password: ")
    if user in users and password == users[user]["password"]:
        print("Bienvenido,", users[user]["nombre"])
        break
    else:
        print("User or password invalid")

rol = users[user]["rol"]

# MENU ESTUDIANTE
if rol == "alumno":
    passed = set()
    print(f"\nGrades of {users[user]['nombre']}")
    for subject in subjects:
        # Corregido: Imprimir la materia individual, no la tupla completa
        print(f"{subject}: {notes[user][subject]}")
        # Corregido: La calificación mínima aprobatoria según el PDF es 8.0
        if notes[user][subject] >= 8.0:
            passed.add(subject)
            
    not_passed = set(subjects) - passed
    print("\nPassed:", passed)
    print("Not passed:", not_passed)

# MENU MAESTRO
elif rol == "maestro":
    print("\nRol:", users[user]["rol"])
    print("Students:")
    # Corregido: Cambiar 'user' por 'estudiante' para no perder el login
    for estudiante in notes:
        print(f"- {users[estudiante]['nombre']} ({estudiante})")
    
    print("\nSubjects:")
    for subject in subjects:
        print(f"- {subject}")
        
    change = input("\nDo you want to change a student grade? (yes/no): ")
    while change.lower() == "yes":
        student = input("Student username: ")
        subject = input("Subject name: ")
        
        if student in notes and subject in subjects:
            new = float(input("New grade: "))
            confirmation = input("Sure? (yes/no): ")
            # Corregido: Validar contra 'yes' que coincide con tu prompt
            if confirmation.lower() == "yes":
                notes[student][subject] = new
                print("Grade updated successfully.\n")
                print(f"New grades for {users[student]['nombre']}:")
                for subj in subjects:
                    print(f"{subj}: {notes[student][subj]}")
        else:
            print("Student or Subject invalid")
            
        change = input("\nDo you want to change another grade? (yes/no): ")

# MENU COORDINADOR
elif rol == "coordinador":
    print("\n--- COORDINATOR REPORT ---")
    print("Teachers:")
    for usuario, datos in users.items():
        if datos["rol"] == "maestro":
            print(f"- {datos['nombre']}")
            
    print("\nSubjects:")
    for subject in subjects:
        print(f"- {subject}")
        
    print("\nStudents Grades:")
    # Corregido: Formato dinámico y limpio para mostrar todas las materias de tus alumnos
    for student, student_notes in notes.items():
        print(f"\nStudent: {users[student]['nombre']}")
        for subject in subjects:
            print(f"  {subject:45} | {student_notes[subject]}")