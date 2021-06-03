var mapFunction = function() {
    if (this.PLACES != null){

    
	for (var i = 0; i < this.PLACES.length; i++) {
		var key = this.PLACES[i];
		var value = {
			subtotal: 1//count(this.PLACES[i])
            
			}

		/* Función emit para agregar un valor a la clave */
		emit(key, value);
		}
    }
	};

var reduceFunction = function(id, countObjVals) {
    reducedVal = { total: 0 };

    for (var i = 0; i < countObjVals.length; i++) {
        reducedVal.total += countObjVals[i].subtotal;
        }

    return reducedVal;
    };


db.reuterCollection.mapReduce(
    mapFunction,
    reduceFunction,
    {out:'map1'}
    );

    //C:\Users\ulirp\OneDrive - Estudiantes ITCR\Cursos TEC\Primer Semestre 2021\Bases de atos II\Proyectos\TPR3\2021-1 TP3 - Noticias Reuters - MongoDB\Parseo\jsonMiedo2.json
