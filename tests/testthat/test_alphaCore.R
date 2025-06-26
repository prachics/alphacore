# test_alphaCore.R
library(testthat)
library(igraph)
library(data.table)
source("../../algorithms/alphaCore.R")


# Test 1: Default parameters
test_that("Default parameters: ", {
    # Set seed for reproducibility
    set.seed(1)

    g <- erdos.renyi.game(200, 2 / 200, directed = T)
    E(g)$weight <- 1:ecount(g)
    V(g)$name <- paste("v", 1:vcount(g), sep = "")

    # Run alphaCore
    result <- alphaCore(g)

    # Test that result has correct structure
    expect_true(all(c("node", "alpha", "batch") %in% names(result)))
    expect_equal(nrow(result), 200)
    expect_true(all(result$alpha >= 0 & result$alpha <= 1))
    expect_true(all(result$batch >= 0))

    print(head(result, 5))
    print(tail(result, 5))
})

# Test 2: Custom features
test_that("Custom features: ", {
    # Set seed for reproducibility
    set.seed(1)

    g <- erdos.renyi.game(200, 2 / 200, directed = T)
    E(g)$weight <- 1:ecount(g)
    V(g)$name <- paste("v", 1:vcount(g), sep = "")

    result <- alphaCore(g, features = c("indegree", "triangles"))

    # Test that result has correct structure
    expect_true(all(c("node", "alpha", "batch") %in% names(result)))
    expect_equal(nrow(result), 200)
    expect_true(all(result$alpha >= 0 & result$alpha <= 1))
    expect_true(all(result$batch >= 0))

    print(head(result, 6))
    print(tail(result, 5))
})
