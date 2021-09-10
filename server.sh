export FLASK_APP=app
export FLASK_ENV=development

set -o allexport
source ./.env
set +o allexport

flask run
