validateAddress :: String -> Either AddressParseError ValidAddress

fn validateAddress(address: String) -> Result<AddressParseError, ValidAddress> {

}

func validateAndSignup(user: User) async {
    userService.validate(user)
        .flatMap { validatedUser in  await signup(validatedUser) }
        .flatMap { userRecord in doSomething(userRecord) }
        .flatMap { something in doSomethingElse(userRecord) }
        .flatMap { anotherThing in doAnotherThing(something) }
}

func validateAndSignup(user: User) {
    switch userService.validate(user) {
        case success(let validatedUser):
            switch await signup(validatedUser) {
                case success(let userRecord):
                    // do something
                case failure(let error):
                    // handle error
            }
        case failure(let error):
            // handle error
    }
}

func signup(user: ValidatedUser) async throws {
    let saltedHashedPassword = hashService.hash(user.password, salt: hashService.genSalt(10))
    try await db.insert(user, saltedHashedPassword)
}
////////////////////////////////////////////////////////////////////////////////////////////////////

func signup(user: User) async throws {
    let saltedHashedPassword = hashService.hash(user.password, salt: hashService.genSalt(10))
    let validatedUser = try userService.validate(user)
    try await db.insert(validatedUser, saltedHashedPassword)
}

async func signup(user: User) -> Result<UserRecord, Error> {
    guard let validatedUser = userService.validate(user) else { return .failure(UserNotValidatedError) }
    let saltedHashedPassword = hashService.hash(user.password, salt: hashService.genSalt(10))
    return await db.insert(validatedUser, saltedHashedPassword)
}

User.signup = { user in
	 Promise { resolve, reject in
		User.validate(user)
            .then { Bcrypt.genSalt(10) }
            .then { salt in Bcrypt.hash(user.password, salt, null) }
            .then { saltedHashedPassword in User.insertIntoDatabase(user, saltedHashedPassword) }
            .then { userRecord in resolve(userRecord) }
            .catch { error in reject(error) }
	}
}


User.signup = function(user) {
	return new Promise(function(resolve, reject) {
		User.validate(user)
		.then(function() {
			return Bcrypt.genSalt(10);
		}).then(function(salt) {
			return Bcrypt.hash(user.password, salt, null);
		}).then(function(saltedHashedPassword) {
			return User.insertIntoDatabase(user, saltedHashedPassword);
		}).then(function(userRecord) {
			resolve(userRecord);
		}).catch(function(error) {
			reject(error);
		});
	});
};