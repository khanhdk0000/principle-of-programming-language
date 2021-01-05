.source BKITClass.java
.class public BKITClass
.super java.lang.Object
.field static a I
.field static b Ljava/lang/String;
.field static c F

.method public static main([Ljava/lang/String;)V
	iconst_5
	putstatic BKITClass/a I
	ldc "string"
	putstatic BKITClass/b Ljava/lang/String;
	ldc 5.6
	putstatic BKITClass/c F
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	ldc "random"
	invokestatic BKITClass/f1(Ljava/lang/String;)V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static f1(Ljava/lang/String;)V
.var 0 is x Ljava/lang/String; from Label0 to Label1
Label0:
	ldc "yea"
	invokestatic io/print(Ljava/lang/String;)V
	return
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public <init>()V
.var 0 is this LBKITClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
