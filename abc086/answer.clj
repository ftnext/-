(defn is_even_product? [first second]
  (if (even? first) (println "Even")
    (if (even? second) (println "Even") (println "Odd"))))

(is_even_product? (read) (read))
