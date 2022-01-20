# Django

 IN This project, I created School Management System using django sqlite and django  with langauge python and HTML.

for run :


step=1) 
    1.1) if .env not present in dir please create virtualenv first.
                                OR
    1.2) if .env present in dir. then activate it .
        1.2.1)
                    activate environment
            <<----this environment is create in window OS ---->>>
            a)cd .env
            b)cd scripts
            c)activate
        1.2.2)
                    activate environment
            <<----this environment is create in Linux OS ---->>>
            a)come in dir where enviroment are present
            b)Source (name of enviroment)/bin/activate

    1.1) for deactivate.
        a)cd .env
        b)cd scripts
        c)deactivate

step 2) install requirement.txt fil.

            with cmd ( pip install -r requirements.txt )
            make sure you are in dir. of requirement.txt

step=3) <<<<--- project_name == school
                app_name == student     -->>>>>
         
        Before run please run this cmd for no error:
                1)  (python manage.py makemigrations)
                2)  (python manage.py migrate)

        For run using cmd: (python manage.py runserver)

Note : Before login student , Please change is_active status from admin site(for admin login you have to create Superuser with cmd python manage.py createsuperuser) beacuase by_default is_active is False in database without True is_active you can not login student.



 You can login with first_name = vaibhav and password = vaibhav and check it .

