import { useLazyQuery, gql } from "@apollo/client";

const LOGIN = gql`
  query Login($username: String!) {
    login(username: $username)
  }
`;

function useLoginQuery() {
  return useLazyQuery(LOGIN);
}

export default useLoginQuery;
