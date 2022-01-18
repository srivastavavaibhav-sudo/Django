{% for data in dataset %}
{{data.id}}
{{data.first_name}}
{{data.last_name}}
{{data.phone}}
{{data.age}}
{{data.email}}
{{data.Date_of_birth}}
{{data.status}}
{{data.image}}
<hr>
{% endfor %}

{% for data in dataset %}
{{data.id}}
{{data.first_name}}
{{data.last_name}}
{{data.phone}}
{{data.age}}
{{data.email}}
{{data.Date_of_birth}}
{{data.status}}
{{data.image}}
<hr>
{% endfor %}
<!DOCTYPE html>  
<html lang="en">  
<head>  
    <meta charset="UTF-8">  
    <title>Student Records</title>  
     {% load static %}  
    <link rel="stylesheet" href="{% static 'css/style.css' %}"/>  
</head>  
<body>  
<table class="table table-striped table-bordered table-sm">  
    <thead class="thead-dark">  
    <tr>  
        <th>Student ID</th>  
        <th>Student Name</th>  
        <th>Student Email</th>  
        <th>Student Contact</th>  
        <th>Student ID</th>  
        <th>Student Name</th>  
        <th>Student Email</th>  
        <th>Student Contact</th> 
        <th>Actions</th>  
    </tr>  
    </thead>  
    <tbody>  
                {% for data in dataset %}
    <tr>  
        <td>{{data.id}}</td>  
        <td>{{data.first_name}}</td>  
        <td>{{data.last_name}}</td>  
        <td>{{data.phone}}</td>    
    </tr>  
{% endfor %}  
    </tbody>  
</table>  
<br>  
<br>  
<!-- <center><a href="/emp" class="btn btn-primary">Add New Record</a></center>   -->
</body>  
</html>
