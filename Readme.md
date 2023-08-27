# LinkedIn Messages

With this python code you can press the `Contact` button and send a message to conect with any targeted LinkedIn user you can access.

In this version, this code make a connection to one of my local directories using the method `get_source_path` in the `Contact.py` file. Thi method get many `.txt` files and extract the LinkedIn contact information.

Here a `.txt` content file example:
```
name: Marco Antonio
position: Jefe de Mantenimiento en Alpayana S.A.
link: https://www.linkedin.com/in/marco-antonio-8b754386?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAABI7uUsBTExvxqYkBgGxOv4S1WxiKhgEC6k
page: 4
key_position: mantenimiento

name: Erick Renzo Armas Baldeon
position: Mining Engineer|Mine Planner
link: https://www.linkedin.com/in/erick-renzo-armas-baldeon-114327b6?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAABib1eABh33kG7PZKIV5QDsIWbfIDJHTm2M
page: 1
key_position: planner

name: Ximena G.
position: planner en Cia Minera Casapalca
link: https://www.linkedin.com/in/yhasmin-herrera-casta%C3%B1eda-337179161?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAACalUZsBcKjAayU3SVNYxUPa0Wz9rC4niyo
page: 23
key_position: planner
```

In the V3 I will improve the `get_source_path` method changing it to avoid the local directory connection.

For now, create one or many `.txt` files with the structure shown before in your project and modify the path in the `get_source_path` method in the `Contact.py` to address to that files.