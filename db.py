import sqlite3

connection = sqlite3.connect('database.db')

cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS parametrizacao(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        hora_inicial_ti_seg VARCHAR(10) NOT NULL,
        hora_final_ti_seg VARCHAR(10) NOT NULL,
        hora_inicial_ti_ter VARCHAR(10) NOT NULL,
        hora_final_ti_ter VARCHAR(10) NOT NULL,
        hora_inicial_ti_qua VARCHAR(10) NOT NULL,
        hora_final_ti_qua VARCHAR(10) NOT NULL,
        hora_inicial_ti_qui VARCHAR(10) NOT NULL,
        hora_final_ti_qui VARCHAR(10) NOT NULL,
        hora_inicial_ti_sex VARCHAR(10) NOT NULL,
        hora_final_ti_sex VARCHAR(10) NOT NULL,
        hora_inicial_ti_sab VARCHAR(10) NULL,
        hora_final_ti_sab VARCHAR(10) NULL,
        hora_inicial_ti_dom VARCHAR(10) NULL,
        hora_final_ti_dom VARCHAR(10) NULL          
    );
''')

cursor.execute('''
    INSERT INTO parametrizacao (
               hora_inicial_ti_seg, 
               hora_final_ti_seg, 
               hora_inicial_ti_ter, 
               hora_final_ti_ter,
               hora_inicial_ti_qua,
               hora_final_ti_qua,
               hora_inicial_ti_qui,
               hora_final_ti_qui,
               hora_inicial_ti_sex,
               hora_final_ti_sex
            )
    VALUES (
            '08:00',
            '17:00',
            '08:00',
            '17:00',
            '08:00',
            '17:00',
            '08:00',
            '17:00',
            '08:00',
            '17:00'           
        );
''')

connection.commit()
connection.close()
