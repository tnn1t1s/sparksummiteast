# sparksummiteast
Time Series Talk
intro: why we do it & "the whos who of who cares"
    - Review the RDD
          * distributed, fault tolerant, in memory computations
          * show the type and the operations supported by the type
    - Pair RDD
          * show the type and operations e.g. cogroups
    - introduce time & time series (definition) 
	  * time as a group e.g. partitioning by time w/ Pair RDD
    	  * why is this inefficient
    - Ordered Pair RDD
          * use ordering in partition for efficient operations at scale
          * what operations can we do with an ordered Pair RDD (joins on order)
    - Time Series RDD
          * as-of joins
          * window functions
    - Time Series RDD in Scala 
          * yes, but ... users want python
          * and Pandas
          * which is fine. but toPandas #%%%^$^
    - Time Series in Python
          * examples
          * performance benchmarks
    - Looking Ahead
          * toPandas + Arrow
          * Catalyst work in DF
         
          
