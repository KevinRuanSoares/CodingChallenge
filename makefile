run-app:
	@echo "Iniciando Word Counter APP..."
	cd api && make run & \
	cd web && yarn start & \
	wait