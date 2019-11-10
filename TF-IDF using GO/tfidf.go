go get github.com/wilcosheh/tfidf
glide i

package main

import (
	"fmt"

	"github.com/wilcosheh/tfidf"
	"github.com/wilcosheh/tfidf/seg"
	"github.com/wilcosheh/tfidf/similarity"
)

func main() {

	f := tfidf.New()
	f.AddDocs("how are you", "are you fine", "how old are you", "are you ok", "i am ok", "i am file")

	t1 := "it is so cool"
	w1 := f.Cal(t1)
	fmt.Printf("weight of %s is %+v.\n", t1, w1)

	t2 := "you are so beautiful"
	w2 := f.Cal(t2)
	fmt.Printf("weight of %s is %+v.\n", t2, w2)

	sim := similarity.Cosine(w1, w2)
	fmt.Printf("cosine between %s and %s is %f .\n", t1, t2, sim)

	tokenizer := seg.NewJieba()
	defer tokenizer.Free()

	f = tfidf.NewTokenizer(tokenizer)

	f.AddDocs("I love Go", "I love GoLang", "Simba loves Go")

	t1 = "I love Go"
	w1 = f.Cal(t1)
	fmt.Printf("weight of %s is %+v.\n", t1, w1)

	t2 = "I love GoLang"
	w2 = f.Cal(t2)
	fmt.Printf("weight of %s is %+v.\n", t2, w2)

	sim = similarity.Cosine(w1, w2)
	fmt.Printf("cosine between %s and %s is %f .\n", t1, t2, sim)
}