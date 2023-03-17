# Função para solicitar o caminho para criar o arquivo
solicitarCaminho() {
  echo ">>> Digite o caminho (opcional) para criar o arquivo: "
  read caminho
}

# Função para criar o arquivo no caminho desejado ou no diretório principal
criarArquivo() {
  if [ -z "$caminho" ]; then
    caminho=$(pwd)
  fi
  cp ../Meus_widgets/appBar.txt "$caminho/lib/widgets/NightWolf.dart"
  cp ../Meus_widgets/main.txt "$caminho/lib/widgets/main.dart"
}


# =========================== MAIN.EXE =======================
#solicitarCaminho
#criarArquivo


echo ">>> Digite o nome do projeto: "
read project_name

mkdir $project_name
cd $project_name


#Criando arquivo Flutter
flutter create ${project_name}_app
flutter pub add get
#clear

cd ${project_name}_app

caminho_aplicativo="$(pwd)/$project_name/${project_name}_app"


echo '======================'
echo 'Criando Repositórios...'
echo '======================'

mkdir -p lib/models
mkdir -p lib/widgets
mkdir -p lib/views
mkdir -p lib/pages
mkdir -p lib/controllers
mkdir -p lib/repository

echo '======================'
echo 'Criando Arquivos...'
echo '======================'

touch lib/widgets/CustomAppBar.dart
# Armazenando o caminho atual na variável "caminho"
caminho=$(pwd)

# Adicionando a string à um arquivo no caminho atual



#! Alternativa
# cp /Meus_widgets/appBar.txt $caminho_aplicativo/lib/widgets/CustomAppBar.dart
# cp /Meus_widgets/main.txt $caminho_aplicativo/lib/widgets/main.dart


#Imprimir uma mensagem de sucesso
















