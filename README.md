# Tovarisch Engineer / Blog / Backend

Production: [admin.tovarisch.engineer][production-admin] | [api.tovarisch.engineer][production-api]


## Dev

поставь [hatch](https://hatch.pypa.io/), например с использованием [pipx](https://pipx.pypa.io):

```console
$ pipx install hatch
```

подготовка локального сервера:

```console
$ hatch run dev:init  # конфигурирование gitflow и git hooks
$ hatch run dev:migrate  # миграции django
$ hatch run dev:collectstatic  # сбор статики django
```

запусти дев сервер:

```console
$ hatch run dev:runserver
```

!!! note
	Возможно тебе понадобится создать суперпользователя:

	```console
	$ hatch run dev:django-admin createsuperuser
	```



[production-admin]: https://admin.tovarisch.engineer/
[production-api]: https://api.tovarisch.engineer/
