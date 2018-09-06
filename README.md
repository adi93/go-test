# go-test
My very first vim plugin :)

Generates a test file for '\*.go' files. For example, if your go file name is 'main.go', then this will create 'main\_test.go'

The generated test files contains the stubs for the tests. If a function signature is `func (a Object) functionName (a, b inputType)`, then the generated test stub would be `func TestfunctionName (t *testing.T)`

It also takes care not to add duplicate stubs.

To use it, type ':GenerateTestFile' in the main file.
